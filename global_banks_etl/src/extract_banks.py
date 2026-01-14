import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_att = ["Rank", "Country", "MC_USD_Billion"]


def extract():
    """
    Extracts largest global banks data from archived Wikipedia page.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing:
        - Rank
        - Country
        - MC_USD_Billion (float)
    """

    page = BeautifulSoup(requests.get(url).text, 'lxml')
    df = pd.DataFrame(columns=table_att)

    tables = page.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[1].find('a') is not None:
                table_data = {
                    "Rank": col[0].text.strip(),
                    "Country": col[1].find_all('a')[-1].text.strip(),
                    "MC_USD_Billion": col[2].text.strip()
                }
                df1 = pd.DataFrame(table_data, index=[0])
                df = pd.concat([df, df1], ignore_index=True)

    df['Rank'] = pd.to_numeric(df['Rank'], errors='coerce').astype('Int64')

    # Remove the last character from 'MC_USD_Billion' and convert to float
    df['MC_USD_Billion'] = df['MC_USD_Billion'].str[:-1]
    df['MC_USD_Billion'] = pd.to_numeric(
        df['MC_USD_Billion'],
        errors='coerce'
    ).astype('float')

    return df