# MNIST demo with Docker, Flask, Shiny and Tensorflow
Docker images to demonstrate a Shiny app calling Flask+Tensorflow for model scoring



##Stop/Delete Container

```
docker stop CONTAINER ID
docker rm CONTAINER ID
```

Stop then delete all containers
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```
Delete all images
```
docker rmi $(docker images -q)
```