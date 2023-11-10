#!/usr/bin/env python
# coding: utf-8

# In[20]:



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of samples
n = 44

# England players
player_ids = [i for i in range(1, 45)]
player_names = ['Eoin','Stokes','Buttler','Cook','Birstow','Moeen','Jason','Wood','Archer','Adhil','Root','Warner','Green','Smith','Maxwell','Stoinis','Inglish','Carey','Cummins','Zamba','Warne','Clarke','Kusal','Pathum','Mendis','Mathews','Silva','Chamika','Theekshana','Hasaranga','Chameera','Madushanka','Sanath','Rohit','Gill','Kohli','Rahul','Pandya','Shreyas','Jadeja','Bumrah','Shami','Siraj','Kuldeep']
player_country_ids = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4]
#ordinal type : player grade
player_grade = ['A','A','A','B','B','B','C','C','C','C','C','C','A','A','A','B','B','B','C','C','C','C','C','C','A','A','A','B','B','B','C','C','C','C','C','C','A','A','A','B','B','B','C','C']
# birth date
birth_year = np.random.randint(1990, 2003, n)
birth_month = np.random.randint(1, 13, n)
birth_day = np.random.randint(1, 29, n)
player_dob = [f'{birth_year[i]}-{str(birth_month[i]).zfill(2)}-'
                     f'{str(birth_day[i]).zfill(2)}' for i in range(n)]

# Create DataFrame
df = pd.DataFrame({
    'player_id': player_ids,
    'player_name': player_names,
    'country_id':player_country_ids,
    'player_grade':player_grade,
    'dob':player_dob
})


df.to_csv('player.csv')

get_ipython().system('[title](yourimage.png)')


# In[ ]:





# In[ ]:




