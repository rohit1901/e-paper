from machine import reset, Pin
from utime import sleep
from network import WLAN, STA_IF
import logging

class WLAN_CONNECT:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def __str__(self):
        return f"{self.ssid} {self.password}"
    
    def connect(self):
        #Connect to WLAN
        wlan = WLAN(STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while wlan.isconnected() == False:
            logging.info("Waiting for connection...")
            sleep(1)
        ip = wlan.ifconfig()[0]
        logging.info(f'Connected on {ip}')
        
    def connect_to_wlan(self):
        try:
            LED = Pin("WL_GPIO0", Pin.OUT)
            ip = self.connect()
            LED.on()
            logging.info("LED turned on")
        except KeyboardInterrupt:
            logging.info("LED turned on")
            LED.off()
            logging.error("Interrupted by keystroke. Resetting...")
            reset()

# # Implementation
# ssid = 'CardanoKing'
# password = 'Meissen1960'
# w = WLAN_CONNECT(ssid, password)
# w.connect_to_wlan()