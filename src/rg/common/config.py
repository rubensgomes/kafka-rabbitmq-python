'''This module provides an abstraction to load an application.ini configuration file.

Created on Nov 25, 2022
@author: Rubens Gomes
'''

import errno
import os
import sys

from configparser import ConfigParser

# constants
APP_PROPS_FILE = "kafka-rabbitmq.ini"

class Config(object):
    '''
    A class responsible to load an application configuration file.
    It loads an application configuration from one of the following paths:
        
    1. Local directory. ./kafka-rabbitmq.ini.
    2. User's home directory (~user/kafka-rabbitmq.ini)
    '''

    config = None

    @staticmethod
    def _load_properties():
        '''A private static method used to load configuration file.
        '''
        config = ConfigParser()
        is_loaded = False

        for loc in [ os.curdir, os.path.expanduser("~") ]:

            file = os.path.join(loc, APP_PROPS_FILE)

            try: 
                with open( file ) as source:
                    config.read_file( source )
                    is_loaded = True
            except IOError:
                print("Failed to load file: ", file, file=sys.stderr)
        
        if not is_loaded:
            raise FileNotFoundError( errno.ENOENT, os.strerror(errno.ENOENT), APP_PROPS_FILE )

        return config
    
    config = _load_properties()
