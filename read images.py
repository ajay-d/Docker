import os
import gc
import re
import sys
import psutil
import urllib
import requests

os.environ["KERAS_BACKEND"] = "tensorflow"

from io import BytesIO
from keras import backend as K
from skimage import io, img_as_float
from skimage.transform import rescale, resize

import numpy as np
import pandas as pd

print(sys.version)
print(K.backend())
print(os.getcwd())

if os.path.exists("H:\image-app"):
    os.chdir("H:\image-app")

print(os.getcwd())
root_dir = os.getcwd()
os.chdir(root_dir)

gc.collect()
starting_mem = psutil.virtual_memory().used

dir_list = ['string bikini', 'two-piece swimsuit']

#To hold the directory, image ID and image array
IMAGES = []
for dir in dir_list:
    os.chdir(dir)
    df = pd.read_csv('URLs.csv')
    print(df.shape)
    #for row in np.arange(300):
    for row in np.arange(df.shape[0]):
        mem = psutil.virtual_memory()
        mem_used = (mem.used - starting_mem) / (1024 * 1024 * 1024)
        if row % 10 == 0:
            print(row, round(mem_used, 3) , 'GB')
            print('pct:', psutil.virtual_memory().percent)
        try:
            req = requests.get(df.loc[row, 'url'])
        except Exception as e:
            print('timeout')
        if req.ok:
            try:
                img = io.imread(BytesIO(req.content))
                IMAGES.append((dir, df.loc[row, 'ID'], img_as_float(img)))
            except Exception as e:
                print('row', row)
        #if mem_used > 5:
        if psutil.virtual_memory().percent > 90:
            df_image = pd.DataFrame(IMAGES, columns=['dir', 'ID', 'image'])
            df_image.to_csv('image_arrays.csv', header=False, mode='a')
            IMAGES.clear()
            del df_image
            gc.collect()
            print('memory freed')
    df_image = pd.DataFrame(IMAGES, columns=['dir', 'ID', 'image'])
    df_image.to_csv('image_arrays.csv', header=False, mode='a')
    os.chdir('..')

df_binary = pd.DataFrame(IMAGES, columns=['label', 'ID', 'image'])
os.chdir(root_dir)
df_binary.to_csv('Images.csv', index = False)

row
df.loc[row, 'ID']
len(IMAGES)
io.imsave('test_float.jpg', IMAGES[281][2])
img.shape
print(row)
io.imsave('test.jpg', img)
io.imsave('test_float.jpg', img_as_float(img))
io.imsave('test_resize.jpg', resize(img, (1600, 1600)))

len(IMAGES)
io.imsave('test.jpg',IMAGES[0][2])
