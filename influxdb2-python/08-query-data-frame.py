from influxdb_client import InfluxDBClient, Point, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient.from_config_file("config.ini")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

"""
Prepare data
"""

_point1 = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
_point2 = Point("my_measurement").tag("location", "New York").field("temperature", 24.3)

write_api.write(bucket="my-bucket", record=[_point1, _point2])

"""
Query: using Pandas DataFrame
"""
data_frame = query_api.query_data_frame('from(bucket:"my-bucket") '
                                        '|> range(start: -10m) '
                                        '|> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '
                                        '|> keep(columns: ["location", "temperature"])')
print(data_frame.to_string())

"""
Close client
"""
client.close()