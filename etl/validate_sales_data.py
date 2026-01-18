import pandas as pd

sales_file='Data/processed/clean_sales.csv'
product_file='Data/processed/clean_products.csv'
customer_file='Data/processed/clean_customer.csv'
output_file='Data/processed/final_sales.csv'


def validate_sales_data():
    sales=pd.read_csv(sales_file)
    product=pd.read_csv(product_file)
    customer=pd.read_csv(customer_file)

    print("sales count before validation:",len(sales))

    sales=sales[sales['customer_id'].isin(customer['customer_id'])]

    sales=sales[sales['product_id'].isin(product['product_id'])]

    sales.to_csv(output_file,index=False)
    print("sales count after validation:",len(sales))
    print("final_sales saved:",output_file)
    print(sales)

if __name__ == "__main__":
    validate_sales_data()