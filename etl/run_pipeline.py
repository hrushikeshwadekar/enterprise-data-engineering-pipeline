import os

print("----------------- Pipline Started -----------------")
os.system("python etl/reset_warehouse.py")
os.system("python etl/ingest_raw_data.py")
os.system("python etl/transform_sales_data.py")
os.system("python etl/transform_customer_data.py")
os.system("python etl/transform_product_data.py")
os.system("python etl/validate_sales_data.py")
os.system("python etl/load_sales_to_staging.py")
os.system("python etl/create_warehouse_tables.py")
os.system("python etl/load_diamention.py")
os.system("python etl/load_fact_sales.py")

print("---------------- Pipline completed ----------------")