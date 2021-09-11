#!/usr/bin/env python
# coding: utf-8

# # Problem 1

# In[2]:


import time


# In[3]:


import datetime
import calendar


# In[3]:


date1 = datetime.date(2022, 2, 5)
date2 = datetime.date(2021, 1, 5)


# In[9]:


diff = date1 - date2
print("Days: ", diff)
print("Seconds: ", diff.total_seconds())


# # Problem 2

# In[15]:


print("Today is: ", datetime.datetime.today())


# In[24]:


print("Yesterday was: ", datetime.datetime.today() - datetime.timedelta(days=1))


# In[25]:


print("Tomorrow will be: ", datetime.datetime.today() + datetime.timedelta(days=1))


# # Problem 3

# In[ ]:


dt = datetime.datetime.today()
print('Year: ', dt.year)
print('Date: ', dt, type(dt))
print('Time: ', dt.time(), type(dt.time()))
print(dt.date(), type(dt.date()))


# In[35]:


dt = datetime.datetime.today()
print('Date: ', dt)
print('Year: ', dt.year)
print('Month: ', dt.month)
print('Weekday: ', dt.weekday())
print("+5 days: ", datetime.datetime.today() + datetime.timedelta(days=5))
print("+5 seconds: ", datetime.datetime.today() + datetime.timedelta(seconds=5))


# # Problem 4

# In[4]:


dt = datetime.date(1995, 10, 19)
print('Date: ', dt)
print('Year: ', dt.year)
print('Month: ', dt.month)
print('Weekday: ', dt.weekday())
print("Days till: ", dt - datetime.date.today())


# In[7]:


cal = calendar.month(2017, 5)
print(cal)


# In[9]:


yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
print(yesterday)


# In[10]:


add_3days = yesterday + datetime.timedelta(days=3)
print(add_3days)


# In[11]:


sub_2days = yesterday - datetime.timedelta(days=2)
print(sub_2days)

