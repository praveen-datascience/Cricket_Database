#!/usr/bin/env python
# coding: utf-8

# In[2]:



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = 1000


# Ordinal data: Age groups
ids = [i for i in range(1, 1001)]
player_id = np.random.randint(1, 44, n)
#interval type : dates
contract_year = ['2010-2012', '2012-2014', '2014-2016', '2016-2018', '2018-2020', '2020-2022','2022-2024']
contract_year_data = np.random.choice(contract_year, n)
#Ratio type : salary
playersalary = np.random.randint(10000, 200000, n)



# Create DataFrame
df = pd.DataFrame({
    
    'id': ids,
    'player_id': player_id,
    'contract_year': contract_year_data,
    'salary': playersalary
})



df.to_csv('player_salary.csv')
                             

get_ipython().system('[title](yourimage.png)')


# In[ ]:





# In[ ]:




