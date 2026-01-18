import pandas as pd

RAW_PATH='Data/raw/Sales/sales.csv'
OUTPUT_PATH='Data/processed/clean_sales.csv'

def clean_data_sales():

    df=pd.read_csv(RAW_PATH)
    print("Row data count:", len(df))


    df=df.dropna(subset=['amount','order_date'])

    df=df.drop_duplicates(subset=['order_id'])

    df['amount']=pd.to_numeric(df['amount'],errors='coerce')

    df=df[df['amount']>0]

    df.to_csv(OUTPUT_PATH,index=False)
    print("clean data count:",len(df))
    print("clean data path:",OUTPUT_PATH)
    print("Clean data showing: ",df)

if __name__ == "__main__":
    clean_data_sales()
