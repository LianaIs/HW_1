#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse


# In[2]:


parser = argparse.ArgumentParser()


# In[3]:


parser.add_argument("text", help="some text", type=str)


# In[47]:


args, unknown = parser.parse_known_args()


# In[48]:


text = args.text


# In[49]:


## https://www.w3resource.com/python-exercises/string/


# In[50]:


i = len(text)
if i >= 7:
    if i % 2 != 0:
        print("The old string: ", args.text)
        print("Middle 3 characters: ", args.text[(len(args.text) // 2)-1:(len(args.text) // 2)+2])
        print("The new string: ", args.text[:(len(args.text) // 2)-1] + args.text[(len(args.text) // 2)-1:(len(args.text) // 2)+2].upper() + args.text[(len(args.text) // 2)+2:])

