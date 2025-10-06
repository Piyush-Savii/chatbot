import uuid
import datetime
from google.cloud import bigquery



bq_client = bigquery.Client()
BQ_Table = "data-analytics-254406.portfolio_chatbot_analytics.events"

def record_event(event_type, user_id, channel_id, request_text="", response_text="", model="", tokens_used=None):
    
    row = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.datetime.utcnow(),
        "event_type": event_type,
        "user_id": user_id,
        "channel_id": channel_id,
        "request_text": request_text,
        "response_text": response_text,
        "model": model,
        "tokens_used": tokens_used,
    }
    errors = bq_client.insert_rows_json(BQ_Table, [row])
    if errors:
        print("BigQuery insert errors:", errors)
   