import pandas as pd
import oracledb
df = pd.read_csv("trips.csv")
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
CREATE TABLE TRIPS (
    TRIP_ID VARCHAR2(50) PRIMARY KEY,
    LOAD_ID VARCHAR2(50),
    DRIVER_ID VARCHAR2(50),
    TRUCK_ID VARCHAR2(50),
    TRAILER_ID VARCHAR2(50),
    DISPATCH_DATE VARCHAR2(50),
    ACTUAL_DISTANCE_MILES NUMBER,
    ACTUAL_DURATION_HOURS NUMBER,
    FUEL_GALLONS_USED NUMBER,
    AVERAGE_MPG NUMBER,
    IDLE_TIME_HOURS NUMBER,
    TRIP_STATUS VARCHAR2(50)
)
""")

df = pd.read_csv("trips.csv")
df = df.where(pd.notnull(df), None)
veriler = [tuple(None if pd.isna(x) else int(x) if isinstance(x, float) and x == int(x) else x for x in row) for row in df.itertuples(index=False)]

try:
    usta_basi.executemany("INSERT INTO TRIPS VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)", veriler)
    conn.commit()
    print("Trips Oracle'a gömüldü!")
except Exception as hata:
    print(hata)
finally:
    usta_basi.close()
    conn.close()