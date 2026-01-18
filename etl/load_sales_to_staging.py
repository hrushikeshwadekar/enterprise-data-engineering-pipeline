import pandas as pd
import sqlite3


db_file='enterprise.db'
data_file='Data/processed/final_sales.csv'

def load_sales_to_staging():
    df=pd.read_csv(data_file)

    conn=sqlite3.connect(db_file)
    cur=conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS stg_sales (
            order_id INTEGER,
            customer_id INTEGER,
            product_id INTEGER,
            amount REAL,
            order_date TEXT
        )
    """)

    df.to_sql("stg_sales",conn,if_exists="append",index=False)
    conn.commit()
    conn.close()
    print("Loaded records in stg_sales:",len(df))

if __name__ == "__main__":
    load_sales_to_staging()
