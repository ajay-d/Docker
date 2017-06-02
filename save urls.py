import os
import sys
import urllib
import requests
import platform

os.environ["KERAS_BACKEND"] = "tensorflow"

from io import BytesIO
from keras import backend as K

print(sys.version)
print(K.backend())
print(os.getcwd())
print(sys.path)

print(sys.version)
print('Python', platform.python_version())

if os.path.exists("H:\image-app"):
    os.chdir("H:\image-app")

print(os.getcwd())

headers = {
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '3205df368d50445ca01087388f1c8b8b',
}
param = urllib.parse.urlencode({
    'q': 'golden retriever',
})



