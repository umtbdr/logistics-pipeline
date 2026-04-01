# logistics-pipeline
# 🚛 Logistics Data Pipeline

End-to-end data pipeline built with Oracle SQL and Python on a real-world logistics dataset.

## 📌 Project Overview
This project analyzes driver performance and fuel efficiency across a logistics operation using a 5-table Oracle database, Python, and Pandas.

**Key Question:** Which drivers generate the most revenue, and how does fuel consumption affect profitability?

## 🗄️ Database Schema
- **DRIVERS** — Driver profiles and employment data
- **TRIPS** — Individual trip records with distance and duration
- **ROUTES** — Route definitions and metadata
- **FUEL_PURCHASES** — Fuel transaction records per trip
- **DRIVER_MONTHLY_METRICS** — Aggregated monthly performance per driver

## 🛠️ Tech Stack
- **Database:** Oracle SQL
- **Language:** Python 3
- **Libraries:** Pandas, Matplotlib, oracledb

## 🔍 Analysis
- Top 10 revenue-generating drivers
- On-time delivery rates by driver
- Fuel consumption vs. revenue correlation

## 📊 Output
- Bar chart: Top earners by total revenue
- Excel report: Full driver performance summary
