from python:3.12-alpine
workdir /app
copy requirements.txt ./
run pip install --no-cache-dir -r requirements.txt


copy src ./src
copy data ./data
copy sql ./sql

copy main.py ./main.py

