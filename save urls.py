import os
import re
import sys
import urllib
import requests
import platform

import numpy as np
import pandas as pd

print(sys.version)
print('Python', platform.python_version())

print(sys.path)
print(os.getcwd())

if os.path.exists("H:\image-app"):
    os.chdir("H:\image-app")

print(os.getcwd())

search_term = 'golden retriever'
#https://docs.microsoft.com/en-us/azure/cognitive-services/bing-image-search/paging-images
n_urls = 10
cur_offset = 0

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
    'offset': cur_offset,
    'mkt': 'en-us',
    #'safeSearch': 'Moderate',
    'safeSearch': 'Off',
})

r = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/images/search?%s" % params, headers=headers)
r.json()['totalEstimatedMatches']

if r.ok:
    RAW = []
    REDIRECT = []
    ID = []
    HW = []
    for i in np.arange(n_urls):
        raw_link = r.json()['value'][i]['contentUrl']
        match_object = re.search('r=(http.+)&', raw_link)
        redirect_link = match_object.group(1)
        redirect_link = re.sub('%2f', '/', redirect_link)
        redirect_link = re.sub('%3a', ':', redirect_link)
        print(redirect_link)
        RAW.append(raw_link)
        REDIRECT.append(redirect_link)
        ID.append(r.json()['value'][i]['imageId'])
        HW.append((r.json()['value'][i]['height'], r.json()['value'][i]['width']))

df = pd.DataFrame(ID, columns=['ID'])
df['url'] = REDIRECT
df['raw_url'] = RAW
df_hw = pd.DataFrame(HW, columns=['height', 'width'])
df = pd.concat([df, df_hw], axis=1)

#df.to_csv('URLs.gzip', index = False, compression='gzip')
df.to_csv('URLs.csv', index = False)
