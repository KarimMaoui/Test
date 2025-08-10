import requests
import pandas as pd

def fetch_nasdaq_ipos():
    """
    Renvoie TOUJOURS un DataFrame avec colonnes ['company','date','source'].
    Si l'API/HTML change ou échoue, on renvoie un DF vide normalisé.
    """
    cols = ["company", "date", "source"]
    try:
        # Endpoint non garanti (Nasdaq change souvent).
        # On tente, puis on normalise si possible.
        url = "https://api.nasdaq.com/api/ipo/calendar"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()

        data_json = r.json()
        upcoming = (data_json.get("data") or {}).get("upcoming") or {}
        rows = upcoming.get("rows") or []

        if not rows:
            return pd.DataFrame(columns=cols)

        df = pd.DataFrame(rows)
        # Ces clés varient fréquemment; on protège chaque étape.
        name_col = None
        for c in ["CompanyName", "companyName", "Company", "company"]:
            if c in df.columns:
                name_col = c
                break
        date_col = None
        for c in ["ExpectedDate", "expectedDate", "Date", "date"]:
            if c in df.columns:
                date_col = c
                break

        if not name_col or not date_col:
            return pd.DataFrame(columns=cols)

        out = pd.DataFrame({
            "company": df[name_col].astype(str),
            "date": df[date_col].astype(str),
            "source": "Nasdaq"
        })
        return out[cols]

    except Exception:
        # En cas d'échec, on renvoie un DF vide normalisé
        return pd.DataFrame(columns=cols)
