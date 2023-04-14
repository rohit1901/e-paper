# (year, month, day, weekday, hours, minutes, seconds, subseconds)
# from utime import localtime

from machine import RTC
import urequests
import json

def parse_time(datetime, utc_offset, weekday):
    time_without_offset = datetime.replace(utc_offset, '')
    yyyy_mm_dd, hh_mm_ss_s = time_without_offset.split('T')
    year, month, day = yyyy_mm_dd.split('-')
    hours, minutes, seconds_full = hh_mm_ss_s.split(':')
    seconds, subseconds = seconds_full.split('.')
    return year, month, day, weekday, hours, minutes, seconds, subseconds

class TimeAPI:
    def __init__(self, year, month, day, weekday, hours, minutes, seconds, subseconds):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.subseconds = subseconds

    def __str__(self):
        return f"{self.year} {self.month} {self.day} {self.weekday} {self.hours} {self.minutes} {self.seconds} {self.subseconds}"

    @classmethod
    def get_time(cls):
        url = "http://worldtimeapi.org/api/timezone/Europe/Berlin"
        response = json.loads(urequests.get(url).text)
        return cls(*parse_time(response['datetime'], response['utc_offset'], response['day_of_week']))

# # Implementation
# t = TimeAPI.get_time()
# # Print the results
# print(t) # Prints "2023 04 08 6 19 16 13 075705"

# rtc = RTC()
# rtc.datetime((int(t.year), int(t.month), int(t.day), int(t.weekday), int(t.hours), int(t.minutes), int(t.seconds), int(t.subseconds)))
# print(localtime())