import requests
import pandas as pd

def fetch_nasdaq_ipos():
    url = "https://api.nasdaq.com/api/ipo/calendar"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return pd.DataFrame()

    data_json = r.json()
    upcoming = data_json.get("data", {}).get("upcoming", {}).get("rows", [])

    df = pd.DataFrame(upcoming)
    if not df.empty:
        df = df.rename(columns={"CompanyName": "company", "ExpectedDate": "date"})
        df["source"] = "Nasdaq"

    return df[["company", "date", "source"]]
