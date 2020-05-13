#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task2
import string
book = open("book.txt","r")
punct = string.punctuation
count = 0
dict = {}
wdict ={0,0}
i=0
for line in book:
  bookline = book.readline()
  bookllow = bookline.lower()
  bookstrip = bookllow.strip()
  for word in bookstrip:
    if word in punct:
      bookstrip = bookstrip.replace(word,"")
  bookword = bookstrip.split()
  print(bookword)
  for wo in bookword:
    dict[count] = wo
    count+=1
while i<count:
  i+=1
  j=0
  while j<count:
    j+=1
    if dict[i] == dict[j]:
      k=dict[i]
      c=0
      wdict.update(k:c)
print("Total of words = ",count)
print(dict)
print(wdict)


# In[ ]:




