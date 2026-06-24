<div align="center">

# 🍬 Soul Foods Sales Visualizer

### Quantium Software Engineering Virtual Experience Program

[![Completion Certificate](https://img.shields.io/badge/Forage-Certificate%20Earned-blueviolet?style=for-the-badge&logo=google-chrome&logoColor=white)](./completion_certificate.pdf)
[![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Plotly%20Dash-4.x-00CC96?style=for-the-badge&logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-yellow?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![CI](https://img.shields.io/badge/CI-Bash%20Script-success?style=for-the-badge&logo=gnubash&logoColor=white)](./)

A fully interactive data visualisation app built for **Soul Foods** to analyse the impact of the Pink Morsel price increase on regional sales — completed as part of the [Quantium Software Engineering Virtual Experience](https://www.theforage.com/) on Forage.

</div>

---

## 🏆 Completion Certificate

> Successfully completed all 5 tasks + the bonus CI task.

📄 **[View Completion Certificate](./completion_certificate.pdf)**

---

## 📋 Project Overview

Soul Foods raised the price of their flagship **Pink Morsel** product on **15 January 2021**. This project:

1. **Processes** raw transactional CSV data to compute daily sales revenue per region
2. **Visualises** the sales trend as an interactive line chart to clearly show the before/after impact of the price change
3. **Tests** the app automatically using Pytest + Selenium
4. **Automates** test execution via a CI-ready bash script

---

## 🗂️ Project Structure

```
quantium-starter-repo/
│
├── data/                        # Raw daily transaction CSVs
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   └── daily_sales_data_2.csv
│
├── assets/
│   └── style.css                # Custom CSS for the Dash app
│
├── process_data.py              # ETL: filters Pink Morsel, computes sales
├── formatted_data.csv           # Cleaned & aggregated output dataset
├── app.py                       # Interactive Dash visualisation app
├── test_app.py                  # Pytest test suite (3 tests)
├── run_tests.sh                 # CI bash script for automated testing
├── requirements.txt             # Python dependencies
├── completion_certificate.pdf   # Forage completion certificate
└── README.md
```

---

## ✅ Tasks Completed

| # | Task | Description |
|---|------|-------------|
| 1 | **Environment Setup** | Cloned repo, created virtual environment, installed dependencies |
| 2 | **Data Processing** | ETL script to filter Pink Morsel rows and compute `sales = quantity × price` |
| 3 | **Dash App** | Built interactive line chart with date-sorted sales data and axis labels |
| 4 | **UI Improvements** | Added region radio buttons (`north`, `east`, `south`, `west`, `all`) + custom CSS styling |
| 5 | **Automated Testing** | Wrote 3 Pytest tests verifying header, chart, and region picker presence |
| ⭐ | **Bonus: CI Script** | Created `run_tests.sh` to activate venv, run pytest, and return exit code 0/1 |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google Chrome (for Selenium-based tests)
- Git Bash or WSL (to run the CI script on Windows)

### 1. Clone the Repository

```bash
git clone https://github.com/RebelRoot/quantium-starter-repo.git
cd quantium-starter-repo
```

### 2. Set Up the Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (Linux / macOS / Git Bash)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the ETL Script

Processes raw CSV files and generates `formatted_data.csv`:

```bash
python process_data.py
```

### 4. Launch the App

```bash
python app.py
```

Then open your browser at **[http://127.0.0.1:8050](http://127.0.0.1:8050)**

---

## 📊 App Features

- **Line Chart** — daily Pink Morsel sales over time, sorted by date
- **Region Filter** — radio buttons to switch between `north`, `east`, `south`, `west`, and `all`
- **Price Increase Marker** — the chart clearly highlights the January 15, 2021 inflection point
- **Custom Styling** — dark-themed, modern UI with smooth layout

---

## 🧪 Running Tests

### Manual

```bash
pytest test_app.py -v
```

### Via CI Script (Bash)

```bash
bash run_tests.sh
```

The script:
1. Activates the virtual environment
2. Runs the full Pytest suite
3. Exits with code `0` (all pass) or `1` (any failure)

**Tests:**
- `test_header_present` — verifies the app title header renders
- `test_visualization_present` — verifies the line chart renders
- `test_region_picker_present` — verifies the radio button group renders

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **Pandas** | Data cleaning & aggregation |
| **Plotly / Dash** | Interactive visualisation framework |
| **Pytest** | Test framework |
| **Selenium + webdriver-manager** | Browser automation for UI tests |
| **Bash** | CI script for automated test execution |

---

## 📜 License

This project was completed as part of the [Quantium Software Engineering Virtual Experience Program](https://www.theforage.com/simulations/quantium/software-engineering-qbnw) on Forage.

---

<div align="center">

Made with ❤️ by **RebelRoot**

</div>
