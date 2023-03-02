import numpy as np 
import pandas as pd

data = pd.read_excel('country_vaccination_stats.xlsx')
list = data["country"].unique()

for name in list:
    NaN_change = data[data["country"]==name]
    new = NaN_change["daily_vaccinations"].min()
    NaN_change.fillna(value=new,inplace=True)
