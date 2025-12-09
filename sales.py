import pandas as pd
import glob

def load_and_combine(path="data/*.xlsx"):
    files = glob.glob(path)
    df = pd.concat([pd.read_excel(f) for f in files], ignore_index=True)
    return df

def clean_data(df):
    df.drop_duplicates(inplace=True)
    df["Total"] = df["Quantity"] * df["Unit Price"]
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def summary_report(df):
    summary = {
        "Total Revenue": df["Total"].sum(),
        "Average Order Value": df["Total"].mean(),
        "Total Orders": len(df),
        "Top Region": df.groupby("Region")["Total"].sum().idxmax(),
        "Top Product": df.groupby("Product")["Total"].sum().idxmax(),
    }
    return pd.DataFrame(summary.items(), columns=["Metric", "Value"])

def save_outputs(df, summary):
    df.to_excel("cleaned_sales.xlsx", index=False)
    summary.to_excel("sales_summary.xlsx", index=False)

if _name_ == "_main_":
    df = load_and_combine("sales_raw.xlsx")  # using your single file
    df = clean_data(df)
    summary = summary_report(df)
    save_outputs(df, summary)
    print("Processing complete! Files generated: cleaned_sales.xlsx, sales_summary.xlsx")