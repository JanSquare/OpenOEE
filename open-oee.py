from time import sleep

from config import Config

from influxdb import InfluxDBClient

#Raspberry GPIO
import RPi.GPIO as Gpio


print("Connecting to {}".format(Config.influxdb_host))
IDB = InfluxDBClient(host=Config.influxdb_host, port=8086, username=Config.influxdb_username, password=Config.influxdb_password)

def init():
    # Connect to Database


    #Configue GPIO Pins
    Gpio.setmode(Gpio.BCM)
    Gpio.setup(3, Gpio.IN)
    Gpio.add_event_detect(3, Gpio.FALLING, callback=send_data_for_one_mask, bouncetime=50)
    print("init abgeschlossen")


def send_data_for_one_mask(channel):
    print("Send: one Mask Produced")
    data = "mask,location=MedFacilities,machine=Nucleus,id=id output=1"
    IDB.write_points(data, time_precision='ms', database='MedOEE', protocol='line')


def main():
    sleep(60)
    print("main ended")

if __name__ == "__main__": 
    init()
    while(True):
        main()