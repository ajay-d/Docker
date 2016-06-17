# Basic Shiny Server Image
Lightweight shiny server image with a few R packages<br>

Based off of:
* Ubuntu 16.04 LTS
* R 3.3.0
* Shiny Server 1.4.2.786

##Docker Image:
[R 3.3.0 + Shiny Server](https://hub.docker.com/r/burrito/shiny/)


To start a Shiny application:
```
$ docker run -d -p 3838:3838 -v `path to your appdir`:/srv/shiny-server/ burrito/shiny
```
---

