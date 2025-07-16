# Accident Contributing Factors Visualization

This project analyzes accident data and visualizes how factors like **Time of Day**, **Weather**, and **Road Condition** contribute to the number of accidents.

---

## 🔍 Dataset Overview

- `task05.csv` contains accident records with the following fields:
  - `Time_of_Day`
  - `Weather`
  - `Road_Condition`
  - `Location`
  - `Accidents` (count)

---

## 📊 What It Does

- Groups the accident data by Time of Day, Weather, and Road Condition.
- Sums up accidents under those combinations.
- Visualizes them as a stacked bar chart.

---

## 🧪 How to Run

#### 1. Clone the repo and navigate into the folder:

```bash
   git clone <your-repo-url>
   cd accident_analysis
```

#### 2. Run the program:

```
python main.py
```

---

## 📦 Dependencies:
pandas

matplotlib

#### Install them via:
```
pip install pandas matplotlib
```

---

## 📁 Directory Structure:

```
accident_analysis/
├──  task05.csv
├── visualize.py
├── main.py
└── README.md
```

---

## ✅ Example Output:
A stacked bar chart showing accident distribution based on:

Time of Day

Weather

Road Conditions
