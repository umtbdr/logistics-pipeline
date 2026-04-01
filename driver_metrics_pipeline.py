import pandas as pd
import oracledb
df = pd.read_csv("driver_monthly_metrics.csv")
print(df.dtypes)
print(df.isnull().sum())

conn = oracledb.connect(
    user="system",
    password="Lojistik123",
    dsn="localhost:1521/FREE"
)

usta_basi = conn.cursor()

usta_basi.execute("""
CREATE TABLE DRIVER_MONTHLY_METRICS (
    DRIVER_ID VARCHAR2(50),
    MONTH VARCHAR2(20),
    TRIPS_COMPLETED NUMBER,
    TOTAL_MILES NUMBER,
    TOTAL_REVENUE NUMBER,
    AVERAGE_MPG NUMBER,
    TOTAL_FUEL_GALLONS NUMBER,
    ON_TIME_DELIVERY_RATE NUMBER,
    AVERAGE_IDLE_HOURS NUMBER
)
""")

df = pd.read_csv("driver_monthly_metrics.csv")
df = df.where(pd.notnull(df), None)
veriler = [tuple(None if pd.isna(x) else int(x) if isinstance(x, float) and x == int(x) else x for x in row) for row in df.itertuples(index=False)]

try:
    usta_basi.executemany("INSERT INTO DRIVER_MONTHLY_METRICS VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9)", veriler)
    conn.commit()
    print("Driver metrics Oracle'a gömüldü!")
except Exception as hata:
    print(hata)
finally:
    usta_basi.close()
    conn.close()