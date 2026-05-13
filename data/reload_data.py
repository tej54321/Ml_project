# This file loads CSV data into MySQL with correct TRUE/FALSE conversion

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    print("DB_HOST =", DB_HOST)
    print("DB_PORT =", DB_PORT)
    print("DB_USER =", DB_USER)
    print("DB_PASSWORD =", DB_PASSWORD)
    print("DB_NAME =", DB_NAME)

    url = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    print("DATABASE URL =", url)

    return create_engine(url)

def reload():
    engine = get_engine()

    df = pd.read_csv("data/online_shoppers_intention.csv")

    df['Weekend'] = (
        df['Weekend']
        .astype(str)
        .str.strip()
        .str.upper()
        .map({'TRUE': 1, 'FALSE': 0})
    )

    df['Revenue'] = (
        df['Revenue']
        .astype(str)
        .str.strip()
        .str.upper()
        .map({'TRUE': 1, 'FALSE': 0})
    )

    df.to_sql('online_shoppers', engine, if_exists='replace', index=False)

    print(f"Loaded {len(df)} rows")
    print(df['Revenue'].value_counts())

if __name__ == "__main__":
    reload()