import fastf1
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# enable cache
fastf1.Cache.enable_cache('data/cache')

# load race
session = fastf1.get_session(2023, 'Monaco', 'R')
session.load()

# get laps
laps = session.laps

# select driver
driver_laps = laps.pick_driver('VER')

# select columns
data = driver_laps[['LapNumber','LapTime','Compound']]

# convert lap time to seconds
data['LapTimeSeconds'] = data['LapTime'].dt.total_seconds()

# remove pit laps
data = data[(data['LapTimeSeconds'] > 70) & (data['LapTimeSeconds'] < 90)]

# training data
X = data['LapNumber'].values.reshape(-1,1)
y = data['LapTimeSeconds'].values

# train model
model = LinearRegression()
model.fit(X,y)

# predict future laps
future_laps = np.arange(max(data['LapNumber'])+1, max(data['LapNumber'])+6).reshape(-1,1)

predicted_times = model.predict(future_laps)

print("\nFuture Lap Predictions:\n")

for lap,time in zip(future_laps,predicted_times):
    print(f"Lap {int(lap)} → {time:.2f} sec")

# plot
plt.figure(figsize=(8,5))

plt.scatter(data['LapNumber'],data['LapTimeSeconds'],label="Actual laps")

plt.plot(future_laps,predicted_times,color='red',label="Predicted laps")

plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Future Lap Time Prediction")

plt.legend()
plt.grid(True)

plt.savefig("images/lap_time_prediction.png")
plt.show()