# #FROM python:3.8-slim

# FROM python:3.9

# # Update the package list and install any necessary dependencies
# RUN apt-get update

# # Create a directory for the app
# RUN mkdir /app

# WORKDIR /app

# COPY . /app

# RUN pip install --no-cache-dir -r requirements.txt


# EXPOSE 5000


# CMD ["flask","run", "--host=0.0.0.0", "--port=5000"]



FROM python:3.9-slim

# Install PostgreSQL client utilities
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt  

COPY . .

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
# ENTRYPOINT ["./entrypoint.sh"]


# During  development:  RUN pip install --no-cache-dir -r requirements.txt faster but save the libs locally and re-download them every run.
#Production: For production images use : RUN pip install --no-cache-dir -r requirements.txt