from models.strategy_simulator import calculate_total_strategy_time
from models.plot_utils import plot_multiple_colored_strategies

# Define two example strategies

strategy1 = [
    {"compound": "Medium", "base_lap": 90.0, "degradation": 0.15, "laps": 15},
    {"compound": "Hard", "base_lap": 91.0, "degradation": 0.10, "laps": 20}
]

strategy2 = [
    {"compound": "Soft", "base_lap": 89.0, "degradation": 0.25, "laps": 10},
    {"compound": "Medium", "base_lap": 90.0, "degradation": 0.15, "laps": 10},
    {"compound": "Hard", "base_lap": 91.0, "degradation": 0.10, "laps": 15}
]

strategies = [
    ("1-Stop: Medium → Hard", strategy1),
    ("2-Stop: Soft → Medium → Hard", strategy2)
]

# Plot all strategies together
plot_multiple_colored_strategies(strategies)


#calculate total times
results=[]
for name, strat in strategies:
    total_time = calculate_total_strategy_time(strat)
    results.append((name,total_time))
    print(f"{name} total race time: {total_time:.2f} sec")


# Compare first two starategies
if len(results)>=2:
    name1,time1 = results[0]
    name2,time2 = results[1]
    diff= abs(time1-time2)
    winner = name1 if time1 < time2 else name2
    print(f"\n {winner} is faster by {diff:.2f} seconds.")

