import os

class Config(object):
    influxdb_host = os.getenv("influxdb_host")
    influxdb_username = os.getenv("influxdb_username")
    influxdb_password = os.getenv("influxdb_password")
    sensor_pin = 3