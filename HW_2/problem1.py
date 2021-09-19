#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import datetime


# In[2]:


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", help="number of years", type=int)
parser.add_argument("--num_d", help="number of days", type=int)


# In[5]:


args, unknown = parser.parse_known_args()


# In[ ]:


years = args.num_y or 0
days = args.num_d or 0


# In[20]:


print("Current date: ", datetime.datetime.today())
print("Given years: ", args.num_y)
print("Given days: ", args.num_d)
print("Final date: ", datetime.datetime.today() + datetime.timedelta(days=days) + datetime.timedelta(days=years*365))

