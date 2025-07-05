# analytics.py
import pandas as pd
import os
from datetime import datetime

USER_LOG_PATH = "data/log.csv"

def store_user_data(user_query, chatbot_reply, topic, rating=None):
    if not os.path.exists(USER_LOG_PATH):
        df = pd.DataFrame(columns=["timestamp", "query", "response", "topic", "rating"])
    else:
        df = pd.read_csv(USER_LOG_PATH)
    
    new_row = {
        "timestamp": datetime.now(),
        "query": user_query,
        "response": chatbot_reply,
        "topic": topic,
        "rating": rating
    }
    df = pd.concat([df, pd.DataFrame([new_row])])
    df.to_csv(USER_LOG_PATH, index=False)
