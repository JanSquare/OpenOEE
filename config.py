import os

class Config(object):
    influxdb_host = os.getenv("InfluxdbHost")
    influxdb_username = os.getenv("InfluxdbUser")
    influxdb_password = os.getenv("InfluxdbPassword")
    sensor_pin = 3