from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"
org = "my-org"
token = "kiuEBYPAHnXdQDEdDoK3lUbZD3PLycFY4-QncqfFQKukiU2P0sNAZVKVYzBXTW8jWs7MK-gNyijcFDwDu5zmjw=="
# Store the URL of your InfluxDB instance
url="http://localhost:8086"

#Setup database
client = InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)

## using csv library
csv_result = query_api.query_csv('from(bucket:"my-bucket") |> range(start: -10m)')
val_count = 0
for row in csv_result:
    print (row)
    for cell in row:
        val_count += 1