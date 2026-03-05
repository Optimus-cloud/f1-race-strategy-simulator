def calculate_total_strategy_time(strategy, pit_loss=22.0):
    """
    Calculate total race time for a single strategy.

    strategy: list of stints
        Each stint is a dictionary with:
        - compound
        - base_lap
        - degradation
        - laps

    pit_loss: time loss for a pit stop in seconds

    Returns:
        total_time (float): total race time in seconds
    """
    total_time = 0.0

    for stint in strategy:
        base = stint["base_lap"]
        degr = stint["degradation"]
        laps = stint["laps"]

        # Calculate time for this stint
        stint_time = 0.0
        for i in range(laps):
            lap_time = base + i * degr
            stint_time += lap_time

        total_time += stint_time

    # Number of pit stops = number of stints minus 1
    pit_stops = max(0, len(strategy) - 1)
    total_time += pit_stops * pit_loss

    return total_time
