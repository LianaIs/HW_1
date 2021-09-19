#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse


# In[2]:


parser = argparse.ArgumentParser()


# In[ ]:


parser.add_argument("text", help="some text", type=str)
parser.add_argument("first_word", help="some text", type=str)
parser.add_argument("second_word", help="some text", type=str)


# In[3]:


args, unknown = parser.parse_known_args()


# In[ ]:


print("The given text: ", args.text)
print("First word: ", args.first_word)
print("Second word: ", args.second_word)
print("Output string: " + args.text.replace(args.first_word,args.second_word))

