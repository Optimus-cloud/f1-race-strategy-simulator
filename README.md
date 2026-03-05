# F1 Race Strategy Simulator 

An AI-assisted Formula 1 race strategy simulator built using **real race telemetry data** from the FastF1 API.
The project analyzes driver lap data, models tyre degradation, predicts future lap times, and simulates pit stop strategies to recommend the optimal race strategy.

---

## Project Overview

Formula 1 teams rely heavily on data and simulations to decide race strategies.
This project demonstrates a simplified version of how strategy engineers analyze data and simulate race outcomes.

The simulator:

* Loads real race data using **FastF1**
* Processes lap times for a selected driver
* Models lap time degradation
* Predicts future lap times using **machine learning**
* Simulates multiple pit stop strategies
* Recommends the fastest strategy

---

## Project Pipeline

```
FastF1 Race Data
        ↓
Lap Time Processing
        ↓
Tyre Degradation Modeling
        ↓
Future Lap Time Prediction
        ↓
Strategy Simulation
        ↓
Optimal Pit Stop Recommendation
```

---

## Project Structure

```
F1_Race_Strategy_Simulator
│
├── analysis
│   ├── test_fastf1.py            # Test FastF1 data loading
│   ├── lap_time_predictor.py     # Future lap prediction model
│   └── strategy_optimizer.py     # Strategy simulation & optimization
│
├── models
│   ├── plot_utils.py
│   ├── stint_simulator.py
│   ├── strategy_comparator.py
│   └── strategy_simulator.py
│
├── data
│   └── cache                     # FastF1 cached race data
│
├── main.py                       # Entry script
├── requirements.txt              # Dependencies
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* FastF1 API
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib

---

## Example Output

```
Testing pit stop strategies...

Pit on lap 41 → Total future time: 3033.33 sec
Pit on lap 42 → Total future time: 3034.83 sec
Pit on lap 43 → Total future time: 3036.33 sec

Recommended Strategy:
Pit on lap 41
Expected future race time: 3033.33 sec
```

---

## How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/f1-race-strategy-simulator.git
cd f1-race-strategy-simulator
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run analysis scripts

Load race data:

```
python analysis/test_fastf1.py
```

Predict future lap times:

```
python analysis/lap_time_predictor.py
```

Run strategy optimizer:

```
python analysis/strategy_optimizer.py
```

---

## Future Improvements

Planned upgrades to make the simulator more realistic:

* Tyre compound modelling (Soft / Medium / Hard)
* Pit stop time loss modelling
* Tyre age degradation curves
* Strategy comparison visualization
* Traffic and safety-car simulation
* Reinforcement learning based strategy AI

---

## Author

Varshini
