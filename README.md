To use it you need:
- Docker - https://docs.docker.com/install 
- docker-compose 

All you need is to execute this command
``` docker-compose up -d ```

This will:
- Expose mosquitto broker on your environment on port 1883
- Expose mosquitto broker on your environment on port 9001 (websocket)
- Run mock of button device (sending repeatly random true or false)
- Run mock of dht-12 device (sending repeatly random humidity and temperature value)

