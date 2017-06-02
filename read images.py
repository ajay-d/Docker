import os
import re
import sys
import urllib
import requests

os.environ["KERAS_BACKEND"] = "tensorflow"

from io import BytesIO
from skimage import io, img_as_float
from keras import backend as K

import numpy as np
import pandas as pd

print(sys.version)
print(K.backend())
print(os.getcwd())

if os.path.exists("H:\image-app"):
    os.chdir("H:\image-app")

print(os.getcwd())

dir_list = ['golden retriever']

#To hold the directory, image ID and image array
IMAGES = []
for dir in dir_list:
    os.chdir(dir)
    df = pd.read_csv('URLs.csv')
    print(df.shape)
    for row in np.arange(5):
    #for row in np.arange(df.shape[0]):
        if row % 10 == 0:
            print(row)
        req = requests.get(df.loc[row, 'url'])
        if req.ok:
            img = io.imread(BytesIO(req.content))
            IMAGES.append((dir, df.loc[row, 'ID'], img_as_float(img)))

io.imsave('test.jpg', img)
io.imsave('test2.jpg', img_as_float(img))