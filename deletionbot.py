
# coding: utf-8

# In[6]:

import markovify

# Tact function (c) Molly White, 2013-2016, released MIT License
# https://github.com/molly/CyberPrefixer/blob/master/offensive.py

import offensive


# In[7]:

with open ("deleted-titles-1.txt") as f:
    deltext = f.read()


# In[8]:

deletion_model = markovify.NewlineText(deltext)


# In[9]:

for i in range(100):
    title = deletion_model.make_short_sentence(100)
    if title is not None and offensive.tact(title):
        print(title)


# In[ ]:



