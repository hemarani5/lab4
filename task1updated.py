#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task1
import string
book = open("book2.txt","r")
punct = string.punctuation
for line in book:
  bookline = book.readline()
  bookllow = bookline.lower()
  bookstrip = bookllow.strip()
  for word in bookstrip:
    if word in punct:
      bookstrip = bookstrip.replace(word,"")
  bookword = bookstrip.split()
  print(bookword)


# In[ ]:




