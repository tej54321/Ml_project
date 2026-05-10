import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os

load_dotenv()
print("USER:", os.getenv("DB_USER"))
print("PASSWORD:", os.getenv("DB_PASSWORD"))
print("HOST:", os.getenv("DB_HOST"))
print("PORT:", os.getenv("DB_PORT"))
print("DB:", os.getenv("DB_NAME"))

def get_engine():

    url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME")
    )

    return create_engine(url)

def extract_data():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM online_shoppers",
        engine
    )

    print(f"Extracted {len(df)} rows")

    return df

if __name__ == "__main__":

    df = extract_data()

    print(df.head())