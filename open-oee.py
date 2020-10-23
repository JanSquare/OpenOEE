import time
from influxdb import InfluxDBClient
from random import random
import os

influxdb_host = os.getenv("InfluxdbHost")
influxdb_username = os.getenv("InfluxdbUser")
influxdb_password = os.getenv("InfluxdbPassword")

def init():
    client = InfluxDBClient(host=influxdb_host, port=8086, username=influxdb_username, password=influxdb_password)
    print("init abgeschlossen")


if __name__ == "__main__": 
    init()