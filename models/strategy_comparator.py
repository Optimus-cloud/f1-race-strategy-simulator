from models.strategy_simulator import simulate_race

def compare_strategies(strategies, pit_time):
    """
    Compare multiple race strategies and find the fastest one.

    Parameters:
    - strategies: list of tuples (name, strategy_data)
    - pit_time: seconds lost per pit stop

    Returns:
    - None (prints all results)
    """
    results = []

    for name, strategy_data in strategies:
        total_time, _ = simulate_race(strategy_data, pit_time)
        results.append((name, total_time))

    print("Strategy Comparison:")
    print("--------------------")
    for name, total_time in results:
        print(f"{name}: {total_time} seconds")

    # Find the best (lowest time) strategy
    best = min(results, key=lambda x: x[1])
    print("\nBest Strategy:")
    print(f"{best[0]} → {best[1]} seconds")
