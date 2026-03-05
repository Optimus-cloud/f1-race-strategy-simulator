# models/stint_simulator.py

def simulate_stint(base_lap_time: float, degradation: float, laps: int):
    """
    Simulate a tire stint by calculating lap times with degradation.

    Args:
    - base_lap_time (float): The starting lap time on fresh tires (e.g., 90.0 seconds)
    - degradation (float): How much the lap time increases per lap (e.g., 0.15 sec/lap)
    - laps (int): Number of laps in the stint

    Returns:
    - List of lap times (float)
    """
    lap_times = []
    for lap in range(1, laps + 1):
        lap_time = base_lap_time + degradation * (lap - 1)
        lap_times.append(round(lap_time, 3))
    return lap_times
