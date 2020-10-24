from os import getenv
from time import sleep
from influxdb import InfluxDBClient

#Raspberry GPIO
import RPi.GPIO as GPIO



influxdb_host = os.getenv("InfluxdbHost")
influxdb_username = os.getenv("InfluxdbUser")
influxdb_password = os.getenv("InfluxdbPassword")

def init():
    # Connect to Database
    idb = InfluxDBClient(host=influxdb_host, port=8086, username=influxdb_username, password=influxdb_password)
    print("init abgeschlossen")

    #Configue GPIO Pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




def send_data_for_one_mask():
    idb.write_points("mask, location=MedFacilities, machine=Nucleus, id=id output=1", time_precision='ms', database='MedOEE', protocol='line')

if __name__ == "__main__": 
    init()