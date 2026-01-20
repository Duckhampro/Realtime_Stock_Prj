# Import requirements
import time
import json
import requests
from kafka import KafkaProducer

from kafka.errors import KafkaError
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define variables for API
API_KEY = "d5irt61r01qicq2kfbbgd5irt61r01qicq2kfbc0"
BASE_URL = "https://finnhub.io/api/v1/quote"
SYMBOLS = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN"]
KAFKA_TOPIC = "stock-quotes"
#Initial Producer
try:
    producer = KafkaProducer(
        bootstrap_servers=["localhost:29092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        acks='all',  # Wait for all replicas to acknowledge
        retries=3,
        max_in_flight_requests_per_connection=1
    )
    logger.info("✅ Kafka Producer connected successfully")
except KafkaError as e:
    logger.error(f"❌ Failed to connect to Kafka: {e}")
    exit(1)

#Retrive Data
def fetch_quote(symbol):
    url = f"{BASE_URL}?symbol={symbol}&token={API_KEY}"
    try: 
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        data["symbol"] = symbol
        data["fetched_at"] = int (time.time())
        return data
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None
    
#Looping and Pushing to Stream
while True:
    for symbol in SYMBOLS:
        quote = fetch_quote(symbol)
        if quote:
            print(f"Producing:{quote}")
            future = producer.send(KAFKA_TOPIC, value=quote)
            record_metadata = future.get(timeout=10)
            logger.info(f"✅ Sent {quote['symbol']} to partition {record_metadata.partition} offset {record_metadata.offset}")
    time.sleep(6)