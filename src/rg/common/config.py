# coding: utf-8
"""A class module to load an application configuration file.

This module provides the Config class which leverages the configparser
module to load configuration file similar to what’s found in Microsoft
Windows INI files. 

Typical usage example:

  from rg.common.config import Config

  # use default "application.ini" file
  config = Config()

  # configuration file is called "kafka-rabbitmq.ini"
  config = Config("kafka-rabbitmq.ini")

  bar = foo.FunctionBar()

@see: https://docs.python.org/3/library/configparser.html
@author: Rubens Gomes
"""

import errno
import os
import string_utils
import sys

from configparser import ConfigParser

from .exception import IllegalArgumentException


class Config(object):
    """A class responsible for loading an application INI configuration file.
    """

    def __init__(self, config_file: str ="application.ini"):
        """Inits Config with name of application properties file.

        Parameters:
        ----------
        config_file: str
            The name of the INI configuration file.  It defaults to 
            "application.ini" if not provided.
        """
        if not string_utils.is_full_string(config_file):
            raise IllegalArgumentException(
                "invalid config_file: " + config_file)

        self.config_file = config_file
        self.config = ConfigParser()
        is_loaded = False

        for loc in [os.curdir, os.path.expanduser("~")]:
            file = os.path.join(loc, self.config_file)

            try:
                with open(file) as source:
                    self.config.read_file(source)
                    is_loaded = True
            except IOError:
                print("Failed to load file: ", file, file=sys.stderr)

        if not is_loaded:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), self.config_file)

    def __str__(self):
        """Stringfies the class instance"""
        return str("config_file [{0}]".format(str(self.config_file)))
