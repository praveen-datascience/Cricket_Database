#!/usr/bin/env python
# coding: utf-8

# In[4]:



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Number of samples
n = 13

# Nominal data: country id ,code and country name.
country_ids = [i for i in range(1, 14)]
country_codes = ['ENG','AUS','SL','IND','PAK','AFG','NZ','SA','BAN','WI','ZIM','IRE','SCO']
country_names = ['ENGLAND','AUSTRALIYA','SRILANKA','INDIA','PAKISTAN','AFGHANISTAN','NEWZELAND','SOUTHAFRICA','BANGLADESH','WESTINDIES','ZIMBABWE','IRELAND','SCOTLAND']


# Create DataFrame
df = pd.DataFrame({
    'country_id': country_ids,
    'country_code': country_codes,
    'country_name': country_names
})


df.to_csv('country.csv')

get_ipython().system('[title](yourimage.png)')


# In[ ]:




