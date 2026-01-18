import pandas as pd
import sqlite3

data_file='Data/processed/final_sales.csv'

def load_Fact_data():
    conn=sqlite3.connect('enterprise.db')
    conn.execute("DELETE FROM fact_sales")
    sales=pd.read_csv(data_file)
    dim_customer=pd.read_sql("select customer_key,customer_id from dim_customer",conn)
    dim_product=pd.read_sql("select product_key,product_id from dim_product",conn)
    dim_date=pd.read_sql("select date_key,order_date from dim_date",conn)

    fact=sales.merge(dim_customer, on="customer_id", how="inner").merge(dim_product,on="product_id",how="inner").merge(dim_date,on='order_date',how='inner')

    fact=fact[[
        "order_id","customer_key","product_key","date_key","amount"
    ]]
    
    fact.to_sql("fact_sales",conn,if_exists='append',index=False)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_Fact_data()