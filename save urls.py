import os
import re
import sys
import urllib
import requests
import platform

os.environ["KERAS_BACKEND"] = "tensorflow"

from io import BytesIO
from keras import backend as K

import numpy as np

print(sys.version)
print(K.backend())
print(os.getcwd())
print(sys.path)

print(sys.version)
print('Python', platform.python_version())

if os.path.exists("H:\image-app"):
    os.chdir("H:\image-app")

print(os.getcwd())

search_term = 'golden retriever'
n_urls = 10

headers = {
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '3205df368d50445ca01087388f1c8b8b',
}

if not os.path.exists(search_term):
    os.mkdir(search_term)
os.chdir(search_term)

params = urllib.parse.urlencode({
    'q': search_term,
    'count': n_urls,
    'offset': '0',
    'mkt': 'en-us',
    #'safeSearch': 'Moderate',
    'safeSearch': 'Off',
})

r = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/images/search?%s" % params, headers=headers)

if r.ok:
    for i in np.arange(n_urls):
        raw_link = r.json()['value'][i]['contentUrl']
        match_object = re.search('r=(http.+)&', raw_link)
        redirect_link = match_object.group(1)
        redirect_link = re.sub('%2f', '/', redirect_link)
        redirect_link = re.sub('%3a', ':', redirect_link)
        print(redirect_link)
