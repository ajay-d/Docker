# Docker and Flask
Docker images and Flask demo

##Image:
[Jupyter Notebook + Flask](https://hub.docker.com/r/burrito/flask/)

##Run as
Select a running machine
```
docker-machine ls
eval $(docker-machine env machine_name)
```
Pull image
```
docker pull burrito/flask
```

Windows:
```
winpty docker run -t -i burrito/flask bash
```
Mac:
```
docker run -t -i burrito/flask bash
```