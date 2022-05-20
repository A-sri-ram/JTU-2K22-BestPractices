# Instructions
This assignment consists of a django-rest-framework app that has several violations of common best practices.
The assignment is mostly open-ended, just like the definition of what exactly is a best practice and what's not 😉

Fork this repository and make a new branch named jtu-2k22-<ad_username>, fix as many best practices violations as you can find and make a PR, and assign kushal-ti as the reviewer.

If you don't know anything about django-rest-framework don't worry. You don't have to run the project or make any changes that requires knowledge intimate knowledge of django-rest-framework

## How to run

-- First of All, clone the repository and enter into the folder created

### Install requirements:
--- To install the requirements, run the command : 
 ``` pip3 install -r  requirements.txt ```

### Migrations
--- Run the following commands to run the migrations

1. ``` python manage.py migrate```

### Run the code
--- Build the docker image using ``` docker build -t <tag> . ```

--- Spawn the container by running the following command : 
``` docker run <tag> ``` 