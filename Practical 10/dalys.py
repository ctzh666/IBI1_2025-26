import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path = r"C:\Users\chen\Desktop\Practical 10\dalys-rate-from-all-causes.csv"
dalys_data = pd.read_csv(file_path)
print(dalys_data.iloc[0:10,3:5])#the ninth year max
a=list(dalys_data.iloc[:,0])
for i, value in enumerate(a):
    if value =="Zimbabwe":
        a[i]=True
    else:
        a[i]=False
print(dalys_data.loc[a, 'Year'])#1990~2019
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_dalys = recent_data['DALYs'].idxmax()
country_max = recent_data.loc[max_dalys, 'Entity']
max_dalys = recent_data.loc[max_dalys, 'DALYs']
print(f"max country:{country_max},value:{max_dalys}")
min_dalys = recent_data['DALYs'].idxmin()
country_min = recent_data.loc[min_dalys, 'Entity']
min_dalys = recent_data.loc[min_dalys, 'DALYs']
print(f"min country:{country_min},value:{min_dalys}")
#max country:Lesotho,value:90771.64 
#min country:Singapore,value:15045.11
country_condition = dalys_data['Entity'] == country_max
country_data = dalys_data.loc[country_condition]
plt.figure(figsize=(10, 6))
plt.plot(country_data['Year'], country_data['DALYs'], 'b+-', label=country_max)
plt.title(f'DALYs over time in {country_max}') 
plt.xlabel('Year')
plt.ylabel('DALYs (rate)') 
plt.legend() 
plt.grid(True, linestyle='--', alpha=0.7) 
plt.xticks(country_data['Year'], rotation=45)
plt.tight_layout()
plt.show()
#=====================================================================
low_dalys_condition = dalys_data['DALYs'] < 18000
low_dalys_records = dalys_data.loc[low_dalys_condition, ['Entity', 'Year', 'DALYs']]
num_records = len(low_dalys_records)
if num_records > 0:
    print(low_dalys_records.sort_values(by=['Year', 'Entity']).to_string(index=False))