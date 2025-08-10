import pandas as pd
from .fetch_sec import fetch_sec_ipos
from .config import load_config
from .fetch_nasdaq import fetch_nasdaq_ipos
from .config.py import load_config

def aggregate_sources():
    cfg = load_config()
    sec_df = fetch_sec_ipos(cfg["sec_user_agent"])
    nasdaq_df = fetch_nasdaq_ipos()

    all_df = pd.concat([sec_df, nasdaq_df], ignore_index=True)
    all_df = all_df.drop_duplicates(subset=["company", "date"])
    all_df = all_df.sort_values("date")

    output_path = f"{cfg['output_dir']}/ipo_calendar.csv"
    all_df.to_csv(output_path, index=False)
    print(f"Saved aggregated IPO calendar to {output_path}")
    return all_df
