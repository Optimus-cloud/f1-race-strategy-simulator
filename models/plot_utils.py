import matplotlib.pyplot as plt

def plot_multiple_colored_strategies(strategy_data_list):
    compound_colors = {
        "Soft": "red",
        "Medium": "gold",
        "Hard": "black"
    }

    plt.figure(figsize=(12, 6))

    for strategy_name, strategy in strategy_data_list:
        lap_counter = 1
        for stint in strategy:
            compound = stint["compound"]
            base = stint["base_lap"]
            degr = stint["degradation"]
            laps = stint["laps"]

            lap_times = [base + i * degr for i in range(laps)]
            x = list(range(lap_counter, lap_counter + laps))

            color = compound_colors.get(compound, "gray")

            plt.plot(
                x,
                lap_times,
                color=color,
                label=f"{strategy_name} - {compound} stint"
            )

            lap_counter += laps

    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (sec)")
    plt.title("Lap Time Comparison Across Multiple Strategies")
    plt.grid(True)
    plt.legend()
    plt.show()

