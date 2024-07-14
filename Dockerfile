#FROM python:3.8-slim

FROM python:3.9

# Update the package list and install any necessary dependencies
RUN apt-get update

# Create a directory for the app
RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


CMD ["flask","run", "--host=0.0.0.0", "--port=5000"]
