import pandas as pd

RAW_PATH='Data/Raw/Customer/customer.csv'
OUTPUT_FILE='Data/processed/clean_customer.csv'

def clean_data_customer():
    df=pd.read_csv(RAW_PATH)
    print("Raw data count:",len(df))

    df['customer_id']=pd.to_numeric(df['customer_id'],errors='coerce')

    df=df.dropna(subset=['customer_id'])

    df=df[df['customer_id']>0]

    df=df.drop_duplicates(subset=['customer_id'])

    df['customer_name']=df['customer_name'].fillna('Unknown')
    
    df['city']=df['city'].str.strip().str.upper()

    df.to_csv(OUTPUT_FILE, index=False)
    print("Clean data count:",len(df))
    print("clean data saved:",OUTPUT_FILE)
    print(df)

if __name__ == "__main__":
    clean_data_customer()