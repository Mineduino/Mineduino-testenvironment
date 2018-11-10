TAG=$(date +%F-%H-%M)
docker build -t mineduino/broker:$TAG .
docker tag mineduino/broker:$TAG mineduino/broker:latest
