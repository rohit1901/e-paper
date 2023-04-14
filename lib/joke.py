from machine import reset
import urequests
import json
from constants import joke_url
import logging

def split_string(string):
    """
    Splits a string into multiple strings if it contains more than 50 characters.

    Args:
        string (str): The input string.

    Returns:
        list: A list of strings.
    """
    try:
        logging.info("Splitting joke string")
        if len(string) <= 50:
            return [string]

        result = []
        while len(string) > 50:
            index = string.rfind(' ', 0, 50)
            if index == -1:
                result.append(string[:50])
                string = string[50:]
            else:
                result.append(string[:index])
                string = string[index + 1:]

        result.append(string)
        return result
    except:
        logging.error("Error occurred while splitting joke string: {}".format(string))
        reset()
class Joke:
    def __init__(self, setup, delivery):
        self.setup = setup
        self.delivery = delivery

    def __str__(self):
        return f"{self.setup} {self.delivery}"

    @classmethod
    def get_joke(cls):
        try:
            logging.info("Fetching Joke")
            response = json.loads(urequests.get(joke_url).text)
            return cls(split_string(response['setup']), split_string(response['delivery']))
        except:
            logging.error("Error occurred while fetching Joke.")
            reset()
    
# # Implementation
# joke = Joke.get_joke()
# 
# # Get the joke text
# setup = joke.setup
# delivery = joke.delivery
# 
# # Print the results
# print(setup)  # Prints "some funny joke"