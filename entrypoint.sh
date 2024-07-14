#!/bin/sh

# Exit script in case of error
set -e

# Function to wait for the database to be ready
wait_for_db() {
    echo "Checking if DB is ready..."
    until pg_isready -h db -p 5432 -U postgres; do
        echo "Waiting for the database to become ready..."
        sleep 2
    done
    echo "DB is ready!"
}

# Ensure the database is ready before proceeding
wait_for_db

echo "Running Alembic Upgrades..."
alembic upgrade head

echo "Starting Flask Application..."
exec python main.py
