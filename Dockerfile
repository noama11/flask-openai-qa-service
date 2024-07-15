FROM python:3.9-slim

# Install PostgreSQL client utilities
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements file first for dependency installation
COPY requirements.txt .

RUN pip install -r requirements.txt  

# Copy the rest of the application code
COPY . .


# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Use the entrypoint script
CMD ["./entrypoint.sh"]






# FROM python:3.9-slim

# # Install PostgreSQL client utilities
# RUN apt-get update && apt-get install -y \
#     postgresql-client \
#     && rm -rf /var/lib/apt/lists/*


# WORKDIR /app
# COPY requirements.txt .

# RUN pip install -r requirements.txt  

# COPY . .

# RUN chmod +x entrypoint.sh

# CMD ["./entrypoint.sh"]
# ENTRYPOINT ["./entrypoint.sh"]


# During  development:  RUN pip install --no-cache-dir -r requirements.txt faster but save the libs locally and re-download them every run.
#Production: For production images use : RUN pip install --no-cache-dir -r requirements.txt