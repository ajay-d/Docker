import os
import re
import sys
import urllib
import requests

os.environ["KERAS_BACKEND"] = "tensorflow"

from io import BytesIO
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
