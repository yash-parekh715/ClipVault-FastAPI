#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Replace "www.example.com" with your desired web address
target_url="https://clipvault-fastapi.onrender.com/clip"

# Set the ping interval in seconds (e.g., 10 seconds)
ping_interval=50

while true; do
    ping "$target_url"
    sleep "$ping_interval"
    echo "happening"
done