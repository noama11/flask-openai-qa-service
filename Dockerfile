FROM python:3.9-slim

# Install PostgreSQL client 
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt  


COPY . .



RUN chmod +x entrypoint.sh

# entrypoint script
CMD ["./entrypoint.sh"]




