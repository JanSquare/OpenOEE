## marloth_tech 2020 ##
# Easy Tracker to measure machine output. 
from time import sleep
from accounts import Config
from influxdb import InfluxDBClient
#Raspberry GPIO
import revpimodio2

print("Connecting to {}".format(Config.influxdb_host))
IDB = InfluxDBClient(host=Config.influxdb_host, port=8086, username=Config.influxdb_username, password=Config.influxdb_password)

rpi = revpimodio2.RevPiModIO(autorefresh=True)

def init():
    # Longer Cycletime due to 'long' request
    rpi.cycletime = 50
    # DIO Position in piCtory
    dio = 32

    # Register Event for I_2 
    rpi.io.I_2.reg_event(send_data_for_one_mask, edge=revpimodio2.FALLING)
    print("init complete")

def send_data_for_one_mask(ioname, iovalue):
    print("Send: one Mask Produced")
    mask_data = "mask,location=MedFacilities,machine=Nucleus,id=id output=1"
    IDB.write_points(mask_data, time_precision='ms', database='MedOEE', protocol='line')


def main():
    rpi.mainloop()

if __name__ == "__main__": 
    init()
    while(True):
        main()