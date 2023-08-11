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

query_api = client.query_api()

query = 'from(bucket:"my-bucket")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "my_measurement")\
|> filter(fn: (r) => r.location == "Prague")\
|> filter(fn:(r) => r._field == "temperature" )'

result = query_api.query(org=org, query=query)

results = []
for table in result:
  for record in table.records:
    results.append((record.get_field(), record.get_value()))

print(results)