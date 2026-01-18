import pandas as pd
import sqlite3

conn = sqlite3.connect("enterprise.db")

print("\n--- DATA QUALITY METRICS ---")

raw_sales = pd.read_csv("data/raw/sales/sales.csv")
clean_sales = pd.read_csv("data/processed/clean_sales.csv")
final_sales = pd.read_csv("data/processed/final_sales.csv")

print("Raw sales count      :", len(raw_sales))
print("After cleaning       :", len(clean_sales))
print("After validation     :", len(final_sales))

fact_count = pd.read_sql("SELECT COUNT(*) AS cnt FROM fact_sales", conn)
print("Fact table count     :", fact_count["cnt"][0])

conn.close()
