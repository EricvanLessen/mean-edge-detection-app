from influxdb_client import InfluxDBClient
from influxdb_client.client.query_api import QueryOptions
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient.from_config_file("config.ini")

class ProfilersCallback(object):
    def __init__(self):
        self.records = []

    def __call__(self, flux_record):
        self.records.append(flux_record.values)

callback = ProfilersCallback()

query_api = client.query_api(query_options=QueryOptions(profilers=["query", "operator"], profiler_callback=callback))
tables = query_api.query('from(bucket:"my-bucket") |> range(start: -10m)')

for profiler in callback.records:
    print(f'Custom processing of profiler result: {profiler}')