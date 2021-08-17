import pandas as pd
df = pd.read_excel('C:/Users/gkdud/PycharmProjects/TeamProject/Scraping/files/tech_scraping.xlsx')

import sqlite3
connect = sqlite3.connect('./wadizdb.sqlite3')
df.to_sql('table_tech', connect, if_exists='append', index=False)

connect.close()