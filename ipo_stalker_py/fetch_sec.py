import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_sec_ipos(user_agent):
    url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=S-1&count=100"
    headers = {"User-Agent": user_agent}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    rows = soup.find_all("tr")

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) >= 4:
            filing_date = cols[3].text.strip()
            company_name = cols[1].text.strip()
            data.append({"company": company_name, "date": filing_date, "source": "SEC"})

    return pd.DataFrame(data)
