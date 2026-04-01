import pandas as pd
import oracledb
df = pd.read_csv("fuel_purchases.csv")
print(df.dtypes)
print(df.isnull().sum())


conn = oracledb.connect(
    user="system",
    password="Lojistik123",
    dsn="localhost:1521/FREE"
)

usta_basi = conn.cursor()

usta_basi.execute("""
CREATE TABLE FUEL_PURCHASES (
    FUEL_PURCHASE_ID VARCHAR2(50) PRIMARY KEY,
    TRIP_ID VARCHAR2(50),
    TRUCK_ID VARCHAR2(50),
    DRIVER_ID VARCHAR2(50),
    PURCHASE_DATE VARCHAR2(50),
    LOCATION_CITY VARCHAR2(100),
    LOCATION_STATE VARCHAR2(50),
    GALLONS NUMBER,
    PRICE_PER_GALLON NUMBER,
    TOTAL_COST NUMBER,
    FUEL_CARD_NUMBER VARCHAR2(50)
)
""")

df = pd.read_csv("fuel_purchases.csv")
df = df.where(pd.notnull(df), None)
veriler = [tuple(None if pd.isna(x) else int(x) if isinstance(x, float) and x == int(x) else x for x in row) for row in df.itertuples(index=False)]

try:
    usta_basi.executemany("INSERT INTO FUEL_PURCHASES VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)", veriler)
    conn.commit()
    print("Fuel purchases Oracle'a gömüldü!")
except Exception as hata:
    print(hata)
finally:
    usta_basi.close()
    conn.close()