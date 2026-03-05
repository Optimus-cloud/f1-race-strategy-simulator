import fastf1
import pandas as pd
import matplotlib.pyplot as plt

# enable cache
fastf1.Cache.enable_cache('data/cache')

# load race session
session = fastf1.get_session(2023, 'Monaco', 'R')
session.load()

# get all laps
laps = session.laps

# choose a driver (VER = Verstappen)
driver_laps = laps.pick_driver('VER')

# select useful columns
data = driver_laps[['LapNumber', 'LapTime', 'Compound']]

# convert lap time to seconds
data['LapTimeSeconds'] = data['LapTime'].dt.total_seconds()

# remove pit stop / abnormal laps
data = data[data['LapTimeSeconds'] < 120]

# print first few rows
print("\nDriver Lap Data:\n")
print(data[['LapNumber', 'LapTimeSeconds', 'Compound']].head(10))

# plot tyre degradation
plt.figure(figsize=(8,5))
plt.plot(data['LapNumber'], data['LapTimeSeconds'], marker='o')

plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Tyre Degradation Trend - VER (Monaco 2023)")
plt.grid(True)

plt.savefig("images/lap_time_analysis.png")
plt.show()