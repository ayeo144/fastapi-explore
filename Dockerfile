# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# this creates the working directory inside our container
WORKDIR code/

# copy the pip requirements into our working directory
COPY ./requirements.txt /code/requirements.txt

# install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the API code into the working directory
COPY ./app.py /code/app.py

# run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]