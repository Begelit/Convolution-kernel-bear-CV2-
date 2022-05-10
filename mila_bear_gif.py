#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import os


# In[2]:


path_img_list = os.listdir('/home/koza/bear/era_1')
path_img_list_index = []
path_img_list_sorted = []
for row in path_img_list:
    path_img_list_index+=[int(row.split('.')[0])]
path_img_list_index_sorted = sorted(path_img_list_index)
for row in path_img_list_index_sorted:
    path_img_list_sorted += ['/home/koza/bear/era_1'+'/'+str(row)+'.jpeg']
#print(path_img_list_sorted)


# In[3]:


frames = []
for png in path_img_list_sorted:
    frame = Image.open(png)
    frames.append(frame)


# In[4]:


frames[0].save(
'/home/koza/bear/bear_gif.gif',
save_all = True,
append_images = frames[0:],
optimize = True,
duration = 50,
loop = 0
)


# In[ ]:




