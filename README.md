
# Sales BI Dashboard


A small repo that provides a data pipeline and BI tooling for sales Excel files. Designed to run in Google Colab or locally.


## Features
- Load one or more `.xlsx` files (supports glob patterns)
- Clean and compute `Total` per row
- Save cleaned dataset and a small summary table
- Generate interactive Plotly charts (time series, top products, region pie)
- Create an HTML dashboard (`sales_dashboard.html`)
- Produce a profiling report (`profiling_report.html`) using ydata-profiling
- Interactive dropdown inspector for Colab


## Quick start (Colab)
1. Open a Colab notebook.
2. Upload your `sales_raw.xlsx` (or place multiple `.xlsx` files) using the Colab Files pane or the upload cell.
3. Install dependencies: `!pip install -q plotly ydata-profiling openpyxl ipywidgets`
4. Run `main.py` or paste the code into a Colab cell.


## Quick start (local)
1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Place your Excel files in the project root or in `data/` and run:


```bash
python main.py
