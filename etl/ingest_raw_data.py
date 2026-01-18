import pandas as pd
import os

BASE_PATH = "Data/raw"

def ingest_all_data():
    for folder in ["Sales", "Customer", "Products"]:
        folder_path = os.path.join(BASE_PATH, folder)
        for file in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file)
            df = pd.read_csv(full_path)
            print(f"\nReading {full_path}")
            print(df.head())

if __name__ == "__main__":
    ingest_all_data()
