#!/usr/bin/env python
# coding: utf-8

# In[43]:


import requests
import pandas as pd
import os
import random
from random import randint
import string
import json


# In[3]:


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
print('enter spam url: demo purpose enter https://docs.google.com/forms/d/e/1FAIpQLSc6OnK7OHbQPJSZSBcpRIq2DoCfHi2VIOa3MuzA_DA-ypH9oA/formResponse ')
url =  (input())


# In[35]:


print('enter spam amount: for demo purpose enter 2')
lst = [] 
n =  int(input())
for i in range(0, n): 
  print("Enter ID of",i+1,"demo : entry.1498135098, entry.2606285")
  ele = input()
  lst.append(ele)

df = pd.DataFrame(lst, columns = ['Name']) 
    


# In[50]:


nam = pd.read_json (r'names.json')
domai = pd.read_json (r'mail.json')


# In[52]:

i=1
while i ==1 :
  print("Enter how many entries")
  n=int(input())
  for x in range(n):
    g=randint(0, 3)
    name_extra = ''.join(random.choice(string.digits))
    username = nam[0][randint(0, 999)].lower() + name_extra + '@'+ domai[0][randint(0, 3)].lower()
    password = ''.join(random.choice(chars) for i in range(8))
    requests.post(url, allow_redirects=False, data={
        df['Name'][0]: username,
        df['Name'][1]: password
    })
    print("username",username," Password",password)
  print("do you want to enter more? y=1 n=2")
  i=int(input())

