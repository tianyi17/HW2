#!/usr/bin/env python
# coding: utf-8

# In[1]:


url = "https://data.seattle.gov/api/views/38vd-gytv/rows.csv?accessType=DOWNLOAD"
url_try = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


# In[2]:


from urllib.request import urlretrieve
urlretrieve(url, "flow")
urlretrieve(url_try, "try")
import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv('flow', index_col = 'OBJECTID', parse_dates = True)
data.head()


# In[4]:


#use this data to try the function 
data_try = pd.read_csv('try', index_col = 'Date',parse_dates = True)


# In[5]:


#1 The DataFrame contains only the columns that you specified in #1.
def columns(data_input):
    column_name = ['STNAME', 'COUNT_LOCATION', 'YEAR', 'SEGKEY', 'AAWDT', 'INPUT_STUDY_ID']
    if list(data_input) == column_name:
        return True
    else:
        return False
columns(data)


# In[6]:


#2 The columns contain the correct data type
df = data
data_type = df.dtypes
def types(input):
    if input.dtypes.all() == df.dtypes.all():
        return True
    
    else:
        return False
types(data_try)


# In[7]:


#3 There are at least 10 rows in the DataFrame.
def numbers(data_input):
    if len(data_input) > 10:
        return True
    else:
        return False
numbers(data)
numbers(data_try)


# In[8]:


#Use the data_try to test the above function 


# In[9]:



def columns(data_input):
    column_name = ['STNAME', 'COUNT_LOCATION', 'YEAR', 'SEGKEY', 'AAWDT', 'INPUT_STUDY_ID']
    if list(data_input) == column_name:
        return True
    else:
        return False
columns(data_try)


# In[10]:


df = data
data_type = df.dtypes
def types(input):
    if input.dtypes.all() == df.dtypes.all():
        return True
    
    else:
        return False
types(data_try)


# In[11]:


def numbers(data_input):
    if len(data_input) > 10:
        return True
    else:
        return False
numbers(data_try)

