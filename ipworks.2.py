import pandas as pd
import numpy as np

data = pd.read_csv('country_vaccination_stats.csv')
data.info()

#Q4

print(data.isnull().sum()) #there are 60 null values in daily_vaccinations

country_names = data['country'].unique()

for name in country_names:
    min_daily_vac = data[data['country'] == name].daily_vaccinations.min()
    if pd.isnull(min_daily_vac):
        vac_num = 0             #if there is no min value, there is no valid vaccination num
    else:
        vac_num = min_daily_vac
    data[data['country'] == name] = data[data['country'] == name].fillna(value=vac_num)

data.info() #shows no null val

#Q5

hi_median = {}
for name in country_names[ :3]:
    #keys are the daily vac medians and values are the countries
    #add first three vac medians w/ corresponding countries
    hi_median[(data[data['country'] == name].daily_vaccinations.median())] = name


for name in country_names[3: ]:
    #update the dict, if found a greater daily vac median
    if (data[data['country'] == name].daily_vaccinations.median()) > min(hi_median.keys()):
        hi_median.pop(min(hi_median.keys()))
        hi_median[(data[data['country'] == name].daily_vaccinations.median())] = name

print(hi_median)

#Q6

data['date'] = pd.to_datetime(data['date'])
tot_vac = (data[(data['date'] == '1/6/2021')].daily_vaccinations).sum()
print(tot_vac)






