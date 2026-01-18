import pandas as pd
import sqlite3

conn = sqlite3.connect("enterprise.db")

query = """
SELECT 
    f.order_id,
    d.order_date,
    c.customer_name,
    c.city,
    p.product_name,
    p.category,
    f.amount
FROM fact_sales f
JOIN dim_customer c ON f.customer_key = c.customer_key
JOIN dim_product p  ON f.product_key = p.product_key
JOIN dim_date d     ON f.date_key = d.date_key
"""

df = pd.read_sql(query, conn)
df.to_csv("data/BI/sales_analytics.csv", index=False)

conn.close()
print("BI file exported")
