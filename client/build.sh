TAG=$(date +%F-%H-%M)
docker build -t mineduino/client:$TAG .
docker tag mineduino/client:$TAG mineduino/client:latest
