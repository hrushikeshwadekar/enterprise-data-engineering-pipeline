import sqlite3

conn = sqlite3.connect("enterprise.db")
cur = conn.cursor()

cur.execute("DELETE FROM dim_customer")
cur.execute("DELETE FROM dim_product")
cur.execute("DELETE FROM dim_date")
cur.execute("DELETE FROM fact_sales")

conn.commit()
conn.close()

print("Warehouse tables reset successfully")
