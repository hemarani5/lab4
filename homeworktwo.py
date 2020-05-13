#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
dirroot="/content/sample_data"
Dirlist = []
def dirsearch(dirroot):
  for dirname in os.listdir(dirroot):
    path = os.path.join(dirroot,dirname)
    if os.path.isfile(path):
      Dirlist.append(path)
    else:
      dirname.extend(dirsearch(path))
      return Dirlist
def check_sum(filename):
  cmd = "md5sum" + filename
  fileproc = os.popen(cmd)
  result = fileproc.read()
  status = fileproc.close()
  return result, status
def dupcheck(filenames):
  for file1 in filesnames:
    for file2 in filesnames:
      cmd = 'diff %s %s' % (file1, file2)
      fileproc = os.popen(cmd)
      result = fileproc.read()
      status = fileproc.close()
      if result:
        return False
  return True


# In[ ]:




