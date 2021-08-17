import pandas as pd
df = pd.read_excel('C:/teamproject02/Scraping/files/total_scraping.xlsx')

import sqlite3
connect = sqlite3.connect('./wadizdb.sqlite3')
df.to_sql('table_total', connect, if_exists='append', index=False )



connect.close()