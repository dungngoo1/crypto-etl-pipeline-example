from datetime import datetime
import json
import os


def save_raw(text,folder):
    os.makedirs(folder,exist_ok=True)
    timestamp = datetime.now().strftime("%m%d%Y_%H%M%S")
    path = os.path.join(folder,f"raw_tickers_{timestamp}.json")
    with open(path,"w", encoding="utf-8") as f:
        f.write(text)
    return path

def read_file(path):
    with open(path,"r",encoding="utf-8") as f:
        loaded_json = json.load(f)
    return loaded_json

    