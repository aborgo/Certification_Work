"""
Same as propertyaddress.py but has command line options.
"""

import re
import logging
import configparser
import optparse


config = configparser.RawConfigParser()
config.read('property_address.cfg')
log_filename = config.get('log','output')
log_format = config.get('log','format')
valid_state = config.get('validators','state')
valid_zip_code = config.get('validators','zip_code')
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(level, filename=log_filename):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=log_format)
    logging.info('Starting up the property_address program')

def valid_input(value, regex):
    if regex[len(regex)-1] != '$':
        regex += '$'
    regex = re.compile(regex)
    valid = regex.match(value)
    if not valid:
        return False
    return True

class ZipCodeError(Exception):
    pass
        

class StateError(Exception):
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
        regex = valid_state
        if not valid_input(value,regex):
            msg = 'Invalid State Abbreviation: {}'.format(value)
            logging.error(msg)
            raise StateError
        logging.info('Setting new state')
        self._state = value
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        regex = valid_zip_code
        if not valid_input(value, regex):
            msg = 'Invalid Zip Code: {}'.format(value)
            logging.error(msg)
            raise ZipCodeError
        logging.info('Setting new Zip Code')
        self._zip_code = value

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-l','--level',action='store',dest='level',
                      default='info',
                      help=('Sets the log level to DEBUG, INFO(default),'+ 
                            ' WARNING, ERROR, and CRITICAL'))
    parser.add_option('-n','--name',action='store',dest='name',
                      help='Sets the name value of the Address object')
    parser.add_option('-a','--address',action='store',dest='street_address',
                      help='Sets the street_address value of the Address object')
    parser.add_option('-c','--city',action='store',dest='city',
                      help='Sets the city value of the Address object')
    parser.add_option('-s','--state',action='store',dest='state',
                      help='Sets the state value of the Address object')
    parser.add_option('-z','--zip_code',action='store',dest='zip_code',
                      help='Sets the zip_code value of the Address object')
    (options, args) = parser.parse_args()
    start_logging(level=options.level)
    #enforcing requirements
    opt_list = ['name', 'street_address', 'city', 'state', 'zip_code']
    opt_dict = {}
    for i in opt_list:
        #options isn't iterable so a dict is created
        opt_dict.update({i : options.__getattribute__(i)})
    empty_opts = []
    for i in opt_dict:
        if opt_dict[i] == None:
            short = "-"+i[0]
            empty_opts.append(short)
    if len(empty_opts) == 1:
        msg = 'option {} is required'.format(empty_opts[0])
        logging.error(msg)
        parser.error(msg)
    if len(empty_opts) > 1:
        msg = 'options {} are required'.format(', '.join(empty_opts))
        logging.error(msg)
        parser.error(msg)
    #validation
    if not valid_input(options.state, valid_state):
        msg = 'option -s requires a 3-letter state abbreviation'
        logging.error(msg)
        parser.error(msg)
    if not valid_input(options.zip_code, valid_zip_code):
        msg = "option z requires US zip code of the form 'nnnnn-nnnn'"
        logging.error(msg)
        parser.error(msg)
    home = Address(**opt_dict)
