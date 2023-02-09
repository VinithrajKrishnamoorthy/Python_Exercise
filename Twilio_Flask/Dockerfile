#Use an official Python runtime as the base image
FROM python:3.9-alpine 

# Creating app directory
RUN mkdir /app

#Working directory
WORKDIR /app

#Copy the current directory contents into the container
COPY . /app/

#Install the required packages specified in requirements.txt
RUN pip install -r requirements.txt

#command to run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]