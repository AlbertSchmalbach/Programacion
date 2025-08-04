import pandas as pd
from pathlib import Path

file_home = Path.home()

folder_csv = file_home / 'Documents' / 'Confidencial' / 'ASAMBLEA REGIONAL' / 'csv' 
asam1 = folder_csv /  'asam_1.csv'
asam2 = folder_csv /  'asam_2.csv'

df1 = pd.read_csv(asam1)
df2 = pd.read_csv(asam2)

df1.to_excel(folder_csv / 'asamblea_1.xlsx', sheet_name='asamblea_1', index=False)
df2.to_excel(folder_csv /'asamblea_2.xlsx', sheet_name='asamblea_2', index=False)