from time import sleep

from config import Config

from influxdb import InfluxDBClient

#Raspberry GPIO
import RPi.GPIO as Gpio




def init():
    # Connect to Database
    idb = InfluxDBClient(host=Config.influxdb_host, port=8086, username=Config.influxdb_username, password=Config.influxdb_password)
    

    #Configue GPIO Pins
    Gpio.setmode(Gpio.BCM)
    Gpio.setup(Config.sensor_pin, Gpio.IN)
    Gpio.add_event_detect(Config.sensor_pin, Gpio.RISING, callback=send_data_for_one_mask)
    print("init abgeschlossen")


def send_data_for_one_mask(channel):
    print("Send: one Mask Produced")
    idb.write_points("mask, location=MedFacilities, machine=Nucleus, id=id output=1", time_precision='ms', database='MedOEE', protocol='line')


def main():
    sleep(60)
    print("main ended")

if __name__ == "__main__": 
    init()
    main()