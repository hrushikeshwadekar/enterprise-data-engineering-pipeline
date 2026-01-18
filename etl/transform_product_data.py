import pandas as pd

RAW_FILE='Data/Raw/Products/products.csv'
OUTPUT_FILE='Data/processed/clean_products.csv'

def clean_data_products():

    df=pd.read_csv(RAW_FILE)
    print("Raw data count:",len(df))

    df['product_id']=pd.to_numeric(df['product_id'],errors='coerce')
    df=df.dropna(subset=['product_id'])
    df=df[df['product_id']>0]

    df=df.drop_duplicates(subset=['product_id'])

    df['product_name']=df['product_name'].fillna('Unknown product')
    df['category']=df['category'].fillna('others')

    df['category']=df['category'].str.strip().str.upper()
    df['product_name']=df['product_name'].str.strip().str.upper()

    df.to_csv(OUTPUT_FILE,index=False)
    print("clean data count:", len(df))
    print("clean data saved:", OUTPUT_FILE)

    print(df)

if __name__ == "__main__":
    clean_data_products()

    