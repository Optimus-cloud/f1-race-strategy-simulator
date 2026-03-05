import fastf1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# enable cache
fastf1.Cache.enable_cache('data/cache')

# load race
session = fastf1.get_session(2023, 'Monaco', 'R')
session.load()

laps = session.laps

# choose driver
driver_laps = laps.pick_driver('VER')

# prepare dataframe
data = driver_laps[['LapNumber','LapTime']]

# convert lap time to seconds
data['LapTimeSeconds'] = data['LapTime'].dt.total_seconds()

# remove pit / abnormal laps
data = data[(data['LapTimeSeconds'] > 70) & (data['LapTimeSeconds'] < 90)]

# training data
X = data['LapNumber'].values.reshape(-1,1)
y = data['LapTimeSeconds'].values

# train model
model = LinearRegression()
model.fit(X,y)

# simulate race currently at lap 40
current_lap = 40

race_total_laps = int(session.total_laps)

print("\nTesting pit stop strategies...\n")

best_time = float('inf')
best_pit_lap = None

pit_laps = []
times = []

for pit_lap in range(current_lap+1, current_lap+6):

    total_time = 0

    for lap in range(current_lap+1, race_total_laps+1):

        if lap < pit_lap:
            lap_time = model.predict([[lap]])[0]
        else:
            lap_time = model.predict([[lap]])[0] - 1.5

        total_time += lap_time

    pit_laps.append(pit_lap)
    times.append(total_time)

    print(f"Pit on lap {pit_lap} → Total future time: {total_time:.2f} sec")

    if total_time < best_time:
        best_time = total_time
        best_pit_lap = pit_lap


print("\nRecommended Strategy:")
print(f"Pit on lap {best_pit_lap}")
print(f"Expected future race time: {best_time:.2f} sec")


# -------- Plot Strategy Graph --------

plt.figure(figsize=(8,5))

plt.plot(pit_laps, times, marker='o')

plt.xlabel("Pit Stop Lap")
plt.ylabel("Total Future Race Time (seconds)")
plt.title("Pit Stop Strategy Comparison")

plt.grid(True)

# save graph for GitHub
plt.savefig("images/strategy_comparison.png")

plt.show()