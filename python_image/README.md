# Basic Python Image
Lightweight python image with Flask and Tensorflow<br>
Comes in under 400 MB

Based off of:
* Ubuntu 16.04 LTS
* Python 3.5
* Tensorflow 0.9.0 (CPU only)

##Docker Image:
[Python 3.5 + Tensorflow + Flask](https://hub.docker.com/r/burrito/python/)


To start container interactively:
```
$ docker run -it -p 5000:5000 burrito/python
$ python3
```
---
To run a Python 3 script:
```
$ docker run -it -v `pwd`:/home/work burrito/python python3 script.py
```
---
To run a Flask script:
```
$ docker run -d -p 5000:5000 -v `pwd`:/home/work burrito/python python3 script.py
```