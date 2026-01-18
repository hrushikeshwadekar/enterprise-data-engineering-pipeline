import sqlite3
import pandas as pd

db_file='enterprise.db'
customer_file='Data/processed/clean_customer.csv'
product_file='Data/processed/clean_products.csv'
sale_file='Data/processed/clean_sales.csv'
date_file='Data/processed/final_sales.csv'
conn=sqlite3.connect(db_file)
def load_customer_data():
    
    customer=pd.read_csv(customer_file)
    customer.to_sql('dim_customer',conn,if_exists='append',index=False)
    conn.commit()
    print("customers data loaded in dim_customer")

def load_product_data():
    product=pd.read_csv(product_file)
    product.to_sql('dim_product',conn,if_exists='append',index=False)
    conn.commit()
    print("product data loaded in dim_product")

def load_sales_data():
    sale=pd.read_csv(sale_file)
    sale.to_sql('dim_sale',conn,if_exists='append',index=False)
    conn.commit()
    print("sales data loaded in dim_sale")

def load_date_data():
    date=pd.read_csv(date_file)
    date_df = date[["order_date"]].drop_duplicates()
    date_df.to_sql('dim_date',conn,if_exists='append',index=False)
    conn.commit()
    print("date data loaded in dim_date")

if __name__ == "__main__":
    load_customer_data()
    load_product_data()
    load_sales_data()
    load_date_data()
    conn.close()
    print("all data loaded")

    
