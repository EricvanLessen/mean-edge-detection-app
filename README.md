# mean-edge-detection-app
small app to play with kubernetes, docker, influxDB, nodeJS, python

Run influxDB docker as in https://hub.docker.com/_/influxdb. 
We use a minimal invocation of automated setup is:

$ docker run -d -p 8086:8086 \
      -v $PWD/data:/var/lib/influxdb2 \
      -v $PWD/config:/etc/influxdb2 \
      -e DOCKER_INFLUXDB_INIT_MODE=setup \
      -e DOCKER_INFLUXDB_INIT_USERNAME=my-user \
      -e DOCKER_INFLUXDB_INIT_PASSWORD=my-password \
      -e DOCKER_INFLUXDB_INIT_ORG=my-org \
      -e DOCKER_INFLUXDB_INIT_BUCKET=my-bucket \
      influxdb:2.0

Next we write data to influxdb after reading it into a pandas dataframe:
https://youtu.be/cMkQXLCbFQY. 
You need the python library and the credentials for that.

In the flux query pivot and keep is important for the format and to define what data we keep. 

