# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:39:51 2022

@author: 729sh
"""
import os
imgs = os.listdir('imgs')
import cv2

img = cv2.imread('imgs/'+imgs[0])
crop_img = img[:, :200]
height, width, layers = crop_img.shape  
video = cv2.VideoWriter('Q6.mp4', 0, 1, (width, height))
for x in imgs:
    img = cv2.imread('imgs/'+x)
    crop_img = img[:, :200]
    video.write(crop_img)
cv2.destroyAllWindows() 
video.release()   