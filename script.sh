#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


target_url="https://clipvault-fastapi.onrender.com/clip"


ping_interval=50

while true; do
    ping -c 1 "$target_url"
    sleep "$ping_interval"
done