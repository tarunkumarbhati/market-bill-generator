#!/bin/bash
set -e

app="market"
docker build -t ${app} .
docker run -d -p 8000:8000 \
  --name=${app} \
  -v $PWD:/${app} ${app}

echo "Container started. Run 'sudo docker stop market' to stop the container"
echo "Server running. http://127.0.0.1:8000/"
