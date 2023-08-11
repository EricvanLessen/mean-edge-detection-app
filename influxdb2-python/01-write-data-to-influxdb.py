import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"
org = "my-org"
token = "kiuEBYPAHnXdQDEdDoK3lUbZD3PLycFY4-QncqfFQKukiU2P0sNAZVKVYzBXTW8jWs7MK-gNyijcFDwDu5zmjw=="
# Store the URL of your InfluxDB instance
url="http://localhost:8086"

#Setup database
client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)