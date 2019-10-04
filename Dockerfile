# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /gonculator

# Set the working directory to /gonculator
WORKDIR /gonculator

# Copy the current directory contents into the container at /gonculator
ADD . /gonculator/

# Install any needed packages specified in requirements.txt
RUN pip install --no-index --find-links=file:///gonculator/packages/ -r requirements.txt

#RUN python create_su.py --/home/marclabelle/Projects/env/g.env