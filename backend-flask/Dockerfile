FROM python:3.13.0b2-slim

# Directory within the container
WORKDIR /backend-flask

# copy 'requirements.txt' from the current directory (backend-flask) into the container
COPY requirements.txt requirements.txt

# Run essential libraries in requirements.txt
RUN pip3 install -r requirements.txt

# '.' means everything in the current directory
# first period '.' means current directory (/backend-flask) which is outside container
# second period '.' means with the container (/backend-flask)
COPY . .

# set environment variable (ENV)
# Inside container and will remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD stands for COMMAND
# this command 'python3 -m flask run --host=0.0.0.0 --port=4567'
# uses python3 to run flask module (-m) on all hosts or everything (0.0.0.0) for port number (port) 4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]