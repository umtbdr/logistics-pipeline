import oracledb
import pandas as pd
import matplotlib.pyplot as plt

conn = oracledb.connect(
    user="system",
    password="Lojistik123",
    dsn="localhost:1521/FREE"
)

df = pd.read_sql("""
    SELECT d.FIRST_NAME, d.LAST_NAME, 
           SUM(m.TOTAL_REVENUE) as TOPLAM_GELIR,
           AVG(m.ON_TIME_DELIVERY_RATE) as ZAMANINDA_TESLIMAT,
           SUM(m.TRIPS_COMPLETED) as TOPLAM_SEFER
    FROM DRIVERS d
    INNER JOIN DRIVER_MONTHLY_METRICS m ON d.DRIVER_ID = m.DRIVER_ID
    GROUP BY d.FIRST_NAME, d.LAST_NAME
    ORDER BY TOPLAM_GELIR DESC
""", conn)

print(df.head(10))
df.head(10).plot(
    x="LAST_NAME", 
    y="TOPLAM_GELIR", 
    kind="bar", 
    color="steelblue",
    figsize=(12, 6)
)
plt.title("En Çok Gelir Üreten 10 Sürücü")
plt.xlabel("Sürücü")
plt.ylabel("Toplam Gelir ($)")
plt.tight_layout()
plt.savefig("surucu_analizi.png", dpi=150)
plt.show()
df.to_excel("surucu_raporu.xlsx", index=False)
print("Rapor kaydedildi!")