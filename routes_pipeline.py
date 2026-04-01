import pandas as pd
import oracledb
df = pd.read_csv("routes.csv")
print(df.columns.tolist())
print(df.dtypes)
print(df.isnull().sum())

conn = oracledb.connect(
    user="system",
    password="Lojistik123",
    dsn="localhost:1521/FREE"
)

usta_basi = conn.cursor()

usta_basi.execute("""
CREATE TABLE ROUTES (
    ROUTE_ID VARCHAR2(50) PRIMARY KEY,
    ORIGIN_CITY VARCHAR2(100),
    ORIGIN_STATE VARCHAR2(50),
    DESTINATION_CITY VARCHAR2(100),
    DESTINATION_STATE VARCHAR2(50),
    TYPICAL_DISTANCE_MILES NUMBER,
    BASE_RATE_PER_MILE NUMBER,
    FUEL_SURCHARGE_RATE NUMBER,
    TYPICAL_TRANSIT_DAYS NUMBER
)
""")

df = pd.read_csv("routes.csv")
df = df.where(pd.notnull(df), None)
veriler = [tuple(None if pd.isna(x) else int(x) if isinstance(x, float) and x == int(x) else x for x in row) for row in df.itertuples(index=False)]

try:
    usta_basi.executemany("INSERT INTO ROUTES VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9)", veriler)
    conn.commit()
    print("Routes Oracle'a gömüldü!")
except Exception as hata:
    print(hata)
finally:
    usta_basi.close()
    conn.close()