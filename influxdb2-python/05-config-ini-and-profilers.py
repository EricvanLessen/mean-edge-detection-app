from influxdb_client import InfluxDBClient
from influxdb_client.client.query_api import QueryOptions
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient.from_config_file("config.ini")

q = '''
    from(bucket: stringParam)
      |> range(start: -5m, stop: now())
      |> filter(fn: (r) => r._measurement == "mem")
      |> filter(fn: (r) => r._field == "available" or r._field == "free" or r._field == "used")
      |> aggregateWindow(every: 1m, fn: mean)
      |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
'''
p = {
    "stringParam": "my-bucket",
}

query_api = client.query_api(query_options=QueryOptions(profilers=["query", "operator"]))
csv_result = query_api.query(query=q, params=p)