import requests
import pandas as pd

url = "http://tianqi.2345.com/Pc/GetHistory"

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"""
}

def craw_table(year,month):
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }
    resq = requests.get(url, headers=headers, params=params)
    data = resq.json()["data"]
    df = pd.read_html(data)[0]
    return df

df_list=[]
for year in range(2021,2022):
    for month in range(1,13):
        df = craw_table(year,month)
        df_list.append(df)

pd.concat(df_list).to_excel("北京天气.xlsx",index=False)


