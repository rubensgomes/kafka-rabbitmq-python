# -*- coding: utf-8 -*-
"""A class module to load an application configuration file.

This module provides the Config class which leverages the configparser
module to load a configuration file similar to what’s found in Microsoft
Windows INI files.

The configuration file must be placed in one of the following:

1.  current directory
2.  user's home directory

Typical usage example:

  from rubens_gomes.common.config import Config

  # use default "application.ini" file
  config = Config()

  # configuration file is called "kafka-rabbitmq.ini"
  config = Config("kafka-rabbitmq.ini")

  rabbitmq_url = config.get("RabbitMQ", "url")

@see: https://docs.python.org/3/library/configparser.html
@author: Rubens Gomes
"""

import errno
import os
import string_utils
import sys

from configparser import ConfigParser
from rubens_gomes.common.exception import IllegalArgumentException

INI_FILE = "kafka-rabbitmq.ini"


class Config(object):
    """A class responsible for loading an application INI configuration file.
    """

    def __init__(self, config_file: str = INI_FILE):
        """Initializes an instance of Config with name of application INI file.

        Parameters:
        ----------
        config_file: str
            The name of the INI configuration file.  It defaults to 
            "application.ini" if not provided.

        Raises:
        -------
        FileNotFoundError
            If the config_file is not found or could not be read.
        rubens_gomes.common.exception.IllegalArgumentException
            If the config_file is empty.
        """
        if not string_utils.is_full_string(config_file):
            raise IllegalArgumentException(
                "Invalid config_file: " + config_file)

        self.config_file = config_file
        self.config = ConfigParser()
        is_loaded = False

        for loc in [os.curdir, os.path.expanduser("~")]:
            file = os.path.join(loc, self.config_file)

            try:
                with open(file) as source:
                    self.config.read_file(source)
                    is_loaded = True
            except IOError as error:
                print("Failed to load file: ", file, error, file=sys.stderr)

        if not is_loaded:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), self.config_file)

    def __str__(self):
        """Stringfies the class instance"""
        return str("config_file [{0}]".format(str(self.config_file)))

    def get(self, section: str, option: str) -> str:
        """Retrieves a property from a given section in the application INI file.

        Parameters:
        ----------
        section: str
            The name of the section in the INI configuration file.
        option: str
            The name of the option within the section in the INI configuration file.

        Raises:
        ----------
        rubens_gomes.common.exception.IllegalArgumentException
            If either section or option is empty.
        configparser.NoSectionError:
            If given section is not found in INI file.
        """
        if not string_utils.is_full_string(section):
            raise IllegalArgumentException(
                "Invalid section: " + section)

        if not string_utils.is_full_string(option):
            raise IllegalArgumentException(
                "Invalid option: " + option)

        try:
            return self.config.get(section, option)
        except Exception as error:
            print("Failed to load section/option: ",
                  section, option, error, file=sys.stderr)
            raise ValueError from error
