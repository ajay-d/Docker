FROM jupyter/scipy-notebook
MAINTAINER ajay@deonarine.com

USER root
RUN conda upgrade --all --quiet --yes
RUN conda install --quiet --yes \
    'flask'
	
USER jovyan