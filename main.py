from machine import RTC
import freesans20
from utime import localtime, sleep

from epd3in7 import EPD_3in7
from centerwriter import CenterWriter

from wlanconnect import WLAN_CONNECT
from weather import callAPI, get_display_string_vars, WeatherCode
from timeapi import TimeAPI
from joke import Joke

from constants import ssid, password, display_time_string, axel, coordinates, wind_speed, kmh, deg_c
import logging

def set_time():
    t = TimeAPI.get_time()
    rtc = RTC()
    rtc.datetime((int(t.year), int(t.month), int(t.day), int(t.weekday), int(t.hours), int(t.minutes), int(t.seconds), int(t.subseconds)))
    logging.info("Successfully set time on Board")

if __name__=='__main__':
    # connect to Wi-Fi
    w = WLAN_CONNECT(ssid, password)
    w.connect_to_wlan()
    # Set time
    set_time()
    # Init E-Paper Display
    logging.info("Initializing EPD.")
    epd = EPD_3in7()
    cw = CenterWriter(epd, freesans20)
    cw.set_vertical_spacing(5)
    cw.set_vertical_shift(-30)
    
    while True:
        # Call Weather API
        weather_obj = callAPI()
        windspeed, lat, lon, elevation, temperature, weather_code = get_display_string_vars(weather_obj)
        weather_description = WeatherCode.get_by_code(weather_code).description
        
        # Call Joke API
        joke = Joke.get_joke()
        
        # Get the current time
        logging.info("Formatting time string")
        t = localtime()
        # Format the time as a string
        time_string = display_time_string.format(t[3], t[4], t[2], t[1], t[0])
        # Set display text
        logging.info("Building params to be displayed")
        params = [axel, time_string, coordinates.format(lat, lon), wind_speed.format(windspeed, kmh), "{} {}".format(temperature, deg_c), weather_description]
        params.extend(joke.setup)
        params.extend(joke.delivery)
        
        # Clear display, fill with white color, write text to the display, show the text
        logging.info("Clearing display")
        logging.info("filling with white color")
        logging.info("writing text to the display")
        logging.info("displaying the text")
        epd.clear()
        epd.fill(0xff)
        cw.write_lines(params)
        epd.show()
        logging.info("Sleeping for 60 seconds")
        sleep(60)
    epd.deep_sleep()

