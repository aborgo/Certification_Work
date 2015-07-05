"""
An application that takes in adresses and logs any errors.
"""

import re
import logging

LOG_FILENAME = 'property_address.log'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
DEFAULT_LOG_LEVEL = 'error'
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    logging.info('Starting up the property_address program')


class Error(Exception):
    pass


class ZipCodeError(Error):
    pass
        


class StateError(Error):
    pass

class Address:
    def __init__(self, name,street_address,city,state,zip_code):
        logging.info('Creating new address')
        self._name = name
        self.street_adress = street_address
        self.city = city
        self._state = state
        self._zip_code = zip_code
    
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        regex = re.compile(r"[A-Z][A-Z]")
        valid = regex.match(value)
        if not valid:
            msg = 'Invalid State Abbreviation:{}'.format(value)
            logging.error(msg)
            raise StateError(msg)
        try:
            if valid.group() != value:
                msg = 'Invalid State Abbreviation:{}'.format(value)
                logging.error(msg)
                raise StateError(msg)
        except AttributeError:
            pass
        logging.info('Setting new address')
        self._state = value
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        regex = re.compile(r"\d{5}")
        valid = regex.match(value)
        if not valid:
            msg = 'Invalid Zip Code:{}'.format(value)
            logging.error(msg)
            raise ZipCodeError(msg)
        try:
            if valid.group() != value:
                msg = 'Invalid Zip Code:{}'.format(value)
                logging.error(msg)
                raise ZipCodeError(msg)
        except AttributeError:
            pass
        logging.info('Setting new Zip Code')
        self._zip_code = value

