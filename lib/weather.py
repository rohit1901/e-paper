from machine import reset
import urequests
import json
import logging
from constants import weather_api_url

def callAPI():
    try:
        logging.info("Fetching Weather.")
        response = json.loads(urequests.get(weather_api_url).text)
        return response
    except:
        logging.error("Error fetching weather.")
        reset()

# returns windspeed, lat, lon, elevation, temperature
def get_display_string_vars(weather_obj):
    return weather_obj['current_weather']['windspeed'], weather_obj['latitude'], weather_obj['longitude'], weather_obj['elevation'], weather_obj['current_weather']['temperature'], weather_obj['current_weather']['weathercode']

class WeatherCode:
    def __init__(self, code, description, symbol):
        self.code = code
        self.description = description
        self.symbol = symbol

    def __str__(self):
        return f"{self.code}: {self.description} ({self.symbol})"

    @classmethod
    def get_by_code(cls, code):
        weather_codes = {
            "0": ("Klarer Himmel", "SKC"),
            "1": ("Teilweise bewölkt", "FEW"),
            "2": ("Bewölkt", "SCT"),
            "3": ("Bedeckt", "BKN"),
            "4": ("Nebel", "FG"),
            "5": ("Gefrierender Nebel", "FZFG"),
            "6": ("Leichter Regenschauer", "SHRA"),
            "7": ("Regenschauer", "SHRA"),
            "8": ("Schwerer Regenschauer", "SHRA"),
            "9": ("Gewitter", "TS"),
            "10": ("Leichter Graupelschauer", "SHRASN"),
            "11": ("Graupelschauer", "SHRASN"),
            "12": ("Schwerer Graupelschauer", "SHRASN"),
            "13": ("Leichter Schneeschauer", "SHSN"),
            "14": ("Schneeschauer", "SHSN"),
            "15": ("Schwerer Schneeschauer", "SHSN"),
            "16": ("Hagelschauer", "SHGR"),
            "17": ("Regen", "RA"),
            "18": ("Regen", "RA"),
            "19": ("Starker Regen", "RA"),
            "20": ("Leichter Schneeregen", "SNRA"),
            "21": ("Schneeregen", "SNRA"),
            "22": ("Starker Schneeregen", "SNRA"),
            "23": ("Leichter Schneefall", "SN"),
            "24": ("Schneefall", "SN"),
            "25": ("Starker Schneefall", "SN"),
            "26": ("Hagel", "GR"),
            "27": ("Gewitter", "TS"),
            "28": ("Gewitter", "TS"),
            "29": ("Gewitter", "TS"),
            "30": ("Gewitter", "TS"),
            "31": ("Nebel", "BR"),
            "32": ("Nebel", "FG"),
            "33": ("Gefrierender Nebel", "FZFG"),
            "34": ("Schneetreiben", "BLSN"),
            "35": ("Schneesturm", "BLSN"),
            "36": ("Tornado", "FC"),
            "37": ("Tropischer Sturm", "TS"),
            "38": ("Hurrikan", "HU"),
            "39": ("Tropischer Sturm", "TS"),
            "40": ("Orkanböen", "BKN"),
            "41": ("Schneefall", "SN"),
            "42": ("Schnee", "SN"),
            "43": ("Schneeregen", "SNRA"),
            "44": ("Gefrierender Regen", "FZRA"),
            "45": ("Regen", "RA"),
            "46": ("Regen", "RA"),
            "47": ("Starkregen", "RA"),
            "48": ("Eisregen", "FZRA"),
            "49": ("Nieselregen", "DZ"),
            "50": ("Überfrierende Nässe", "FZDZ"),
            "51": ("Glatteis", "FZDZ"),
            "52": ("Leichter Schneefall", "SN"),
            "53": ("Schneefall", "SN"),
            "54": ("Schwerer Schneefall", "SN"),
            "55": ("Schneeregen", "SNRA"),
            "56": ("Leichter Schneeregen", "SNRA"),
            "57": ("Schwerer Schneeregen", "SNRA"),
            "58": ("Gefrierender Regen", "FZRA"),
            "60": ("Regen", "RA"),
            "61": ("Regen", "RA"),
            "62": ("Starker Regen", "RA"),
            "63": ("Eisregen", "FZRA"),
            "64": ("Gefrierender Regen", "FZRA"),
            "65": ("Schneeregen", "SNRA"),
            "66": ("Leichter Schneeregen", "SNRA"),
            "67": ("Schwerer Schneeregen", "SNRA"),
            "68": ("Gefrierender Regen", "FZRA"),
            "69": ("Nieselregen", "DZ"),
            "70": ("Leichter Schneefall", "SN"),
            "71": ("Schneefall", "SN"),
            "72": ("Starker Schneefall", "SN"),
            "73": ("Schneeregen", "SNRA"),
            "74": ("Leichter Schneeregen", "SNRA"),
            "75": ("Starker Schneeregen", "SNRA"),
            "76": ("Gefrierender Regen", "FZRA"),
            "77": ("Regen", "RA"),
            "78": ("Regen", "RA"),
            "80": ("Leichter Schneefall", "SN"),
            "81": ("Schneefall", "SN"),
            "82": ("Starker Schneefall", "SN"),
            "83": ("Schneeregen", "SNRA"),
            "84": ("Leichter Schneeregen", "SNRA"),
            "85": ("Starker Schneeregen", "SNRA"),
            "86": ("Gefrierender Regen", "FZRA"),
            "87": ("Regen", "RA"),
            "88": ("Regen", "RA"),
            "91": ("Dunst", "BR"),
            "92": ("Nebel", "FG"),
            "93": ("Leichter Regen und Schneeregen", "RASN"),
            "94": ("Regen und Schneeregen", "RASN"),
            "95": ("Starker Regen und Schneeregen", "RASN"),
            "96": ("Leichter Schnee und Schneeregen", "SNRA"),
            "97": ("Schnee und Schneeregen", "SNRA"),
            "98": ("Starker Schnee und Schneeregen", "SNRA"),
            "99": ("Nebel", "FG"),
            "100": ("Stark bewölkt", "OVC")
        }
        description, symbol = weather_codes.get(str(code), ("Unknown", "UNKN"))
        return cls(code, description, symbol)
    
# # Implementation
# # Create a WeatherCode object for code 1
# weather_code = WeatherCode.get_by_code(1)
# 
# # Get the description and symbol
# description = weather_code.description
# symbol = weather_code.symbol
# 
# # Print the results
# print(description)  # Prints "Partly cloudy"
# print(symbol)       # Prints "FEW"