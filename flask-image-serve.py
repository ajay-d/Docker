# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:57:14 2016

@author: adeonari
"""

import base64
import numpy as np
from flask import Flask
from flask import abort, jsonify, request
from keras.models import model_from_json
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# elsewhere...
model = model_from_json(open('/home/ubuntu/cnn_pug_model_architecture.json').read())
model.load_weights('/home/ubuntu/cnn_pug_model_weights.h5')

@app.route('/models/pugs', methods=['POST'])
def score():
    if not request.json or not 'image' in request.json:
        abort(400)
    img_bytes = BytesIO(base64.b64decode(request.json['image']))
    img = np.array(Image.open(img_bytes)).transpose()
    img = img.reshape((1, 3, 224, 224))
    pug_score = model.predict(img)
    print(pug_score)
    return jsonify({'pug_score': str(pug_score[0, 1])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)