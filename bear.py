#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from skimage.io import imread, imsave, imshow
import numpy as np
import cv2


# In[2]:


img_orig = cv2.imread('/home/koza/bear/orig.jpeg')
(B,G,R) = cv2.split(img_orig)
list_orig = [cv2.merge([B,G,R]),cv2.merge([G,B,R]),
             cv2.merge([G,R,B]),cv2.merge([R,G,B]),
             cv2.merge([R,B,G])]
rgb = 0


# In[3]:


kernel = np.array([[0.0,0.0,0.0],
                   [0.0,1.0,0.0],
                   [0.0,0.0,0.0]])
#kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)


# In[4]:


era1_kernel = np.array([[0.0,0.0,0.0],
                         [0.0,0.1,0.0],
                         [0.0,0.0,0.0]])
#era1_kernel = era1_kernel/(np.sum(era1_kernel) if np.sum(era1_kernel) != 0 else 1)


# In[5]:


#kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)
#img_rst = cv2.filter2D(img_orig,-1,kernel)
#cv2.imwrite('/home/koza/bear/era_1/0.jpeg',img_rst)


# In[6]:


for i in range(30):
    kernel += era1_kernel
    text1 = str(kernel[0])
    text2 = str(kernel[1])
    text3 = str(kernel[2])
    text4 = ' - kernel'
    #text = ' '*len('kernel = ')+str(kernel[0])+'\n'+'kernel = '+str(kernel[1])+'\n'+' '*len('kernel = ')+str(kernel[2])
    if rgb > 4:
        rgb = 0
    img_rst = cv2.filter2D(list_orig[rgb],-1,kernel)
    cv2.putText(img_rst,text1,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),2)
    cv2.putText(img_rst,text2,(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),2)
    cv2.putText(img_rst,text3,(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),2)
    cv2.putText(img_rst,text4,(140,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
    #cv2.putText(img_rst,text,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    cv2.imwrite('/home/koza/bear/era_1/'+str(i)+'.jpeg',img_rst)
    if i%10 == 0:
        rgb += 1
    #print(i)
    #print(kernel)


# In[7]:


era2_kernel = np.array([[0.0,-0.1,0.0],
                         [-0.1,0.0,-0.1],
                         [0.0,-0.1,0.0]])
#era2_kernel = era2_kernel/(np.sum(era2_kernel) if np.sum(era2_kernel) != 0 else 1)


# In[8]:


for i in range(i,i+11):
    print(i)
    kernel += era2_kernel
    text1 = str(kernel[0])
    text2 = str(kernel[1])
    text3 = str(kernel[2])
    text4 = ' - kernel'
    if rgb > 4:
        rgb = 0
    img_rst = cv2.filter2D(list_orig[rgb],-1,kernel)
    if i > 34:
        bgr = (0,0,255)
    else:
        bgr = (0,0,0)
    cv2.putText(img_rst,text1,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,bgr,2)
    cv2.putText(img_rst,text2,(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.4,bgr,2)
    cv2.putText(img_rst,text3,(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.4,bgr,2)
    cv2.putText(img_rst,text4,(140,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,bgr,2)
    cv2.imwrite('/home/koza/bear/era_1/'+str(i)+'.jpeg',img_rst)
    if i%10 == 0:
        rgb += 1


# In[9]:


for i in range(i,i+11):
    print(i)
    kernel += era1_kernel
    text1 = str(kernel[0])
    text2 = str(kernel[1])
    text3 = str(kernel[2])
    text4 = ' - kernel'
    #text = ' '*len('kernel = ')+str(kernel[0])+'\n'+'kernel = '+str(kernel[1])+'\n'+' '*len('kernel = ')+str(kernel[2])
    if rgb > 4:
        rgb = 0
    img_rst = cv2.filter2D(list_orig[rgb],-1,kernel)
    if i < 49:
        bgr = (0,0,255)
    else:
        bgr = (0,0,0)
    #cv2.putText(img_rst,text,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    cv2.putText(img_rst,text1,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,bgr,2)
    cv2.putText(img_rst,text2,(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.4,bgr,2)
    cv2.putText(img_rst,text3,(20,60),cv2.FONT_HERSHEY_SIMPLEX,0.4,bgr,2)
    cv2.putText(img_rst,text4,(140,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,bgr,2)
    cv2.imwrite('/home/koza/bear/era_1/'+str(i)+'.jpeg',img_rst)
    if i%10 == 0:
        rgb += 1
    


# In[10]:


for i in range(i,i+11):
    kernel += era1_kernel
    text1 = str(kernel[0])
    text2 = str(kernel[1])
    text3 = str(kernel[2])
    text4 = ' - kernel'
    #text = ' '*len('kernel = ')+str(kernel[0])+'\n'+'kernel = '+str(kernel[1])+'\n'+' '*len('kernel = ')+str(kernel[2])
    if rgb > 4:
        rgb = 0
    img_rst = cv2.filter2D(list_orig[rgb],-1,kernel)
    #cv2.putText(img_rst,text,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    cv2.putText(img_rst,text1,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),2)
    cv2.putText(img_rst,text2,(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),2)
    cv2.putText(img_rst,text3,(20,60),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),2)
    cv2.putText(img_rst,text4,(140,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
    cv2.imwrite('/home/koza/bear/era_1/'+str(i)+'.jpeg',img_rst)
    if i%10 == 0:
        rgb += 1

