import numpy as np 
import pandas as pd

data_excel = pd.read_excel('country_vaccination_stats.xlsx')
data = data_excel.dropna()

list = data["country"].unique()
median_vaccinations = []
for name in list:
    total = data[data["country"]==name]["daily_vaccinations"].mean()
    add = total,name
    median_vaccinations.append(add)
    
median_vaccinations.sort(reverse=True)

for i in range(0,3):
    print(median_vaccinations[i][1])
