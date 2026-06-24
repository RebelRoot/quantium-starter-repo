# Quantium Software Engineering - Soul Foods Sales Visualizer

This repo contains everything you need to get started on the program! Good luck!

## Project Structure
- `.git/`: Official repository history.
- `.gitignore`: Files ignored by git.
- `data/`: Raw daily transaction CSV files (`daily_sales_data_0.csv`, `daily_sales_data_1.csv`, `daily_sales_data_2.csv`).
- `venv/`: Python virtual environment with all required dependencies installed (including Dash, Pandas, Plotly, Pytest, and Dash testing tools).
- `requirements.txt`: Project dependencies.
- `process_data.py`: Data ETL script that processes raw transaction CSVs, filters for "Pink Morsel", calculates sales revenue, and saves the output.
- `formatted_data.csv`: Cleaned, filtered, and aggregated sales dataset containing only `sales`, `date`, and `region`.
- `app.py`: A simple check application to verify your Dash installation.

## How to Run the ETL Script
To re-run the data processing:
1. Open your terminal in this directory.
2. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
3. Run:
   ```bash
   python process_data.py
   ```

## How to Run the App
1. Activate the virtual environment.
2. Run the test app:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:8050/`.
