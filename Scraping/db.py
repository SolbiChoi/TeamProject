import sqlite3
connect = sqlite3.connect('../db.sqlite3')
cursor = connect.cursor()
import pandas as pd
df = pd.read_csv('C:\Develops\TeamProject\Scraping\files')