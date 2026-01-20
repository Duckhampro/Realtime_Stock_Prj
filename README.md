Realtime Stock Data Engineering Project

📌 Overview

This project implements an end-to-end real-time data engineering pipeline for stock market data. The system ingests real-time stock quotes, processes and transforms data using modern DE tools, and serves analytics-ready datasets for visualization.

The project is designed to demonstrate production-style Data Engineering skills including streaming ingestion, orchestration, transformation modeling, and analytics consumption.

🏗️ Architecture

Data Flow:
```
Stock API
│
▼
Kafka
│
▼
MinIO (Raw / Bronze)
│
▼
Snowflake(Raw)
│
▼
dbt run
│
▼
Snowflake(Bronze → Silver → Gold)
│
▼
Apache Superset (Dashboard)
```

🧰 Tech Stack
```
Programming Language: Python

Streaming: Apache Kafka

Orchestration: Apache Airflow

Object Storage: MinIO (S3-compatible)

Data Warehouse: Snowflake

Transformation: dbt (Bronze / Silver / Gold layers)

Visualization: Apache Superset

Containerization: Docker & Docker Compose
```

👤 Author

Duckham
Data Engineer

⭐ If you find this project useful, feel free to star the repository!

