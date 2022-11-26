"""rubens_gomes.common.config.py unit test.

@author Rubens Gomes
"""

from configparser import NoSectionError
from unittest import TestCase

from rubens_gomes.common.config import Config
from rubens_gomes.common.exception import IllegalArgumentException


class Test(TestCase):
    """A unit test class to test the rubens_gomes.common.config functionalities
    """

    def test_fail_constructor_when_empty_config_file(self):
        self.assertRaises(IllegalArgumentException, lambda: Config(" "))

    def test_fail_constructor_when_config_file_not_found(self):
        self.assertRaises(FileNotFoundError,
                          lambda: Config("not_found.ini"))

    def test_success_constructor_when_valid_current_dir_config_file(self):
        config = Config("test.ini")
        self.assertIsInstance(config, Config)

    def test_success_constructor_when_valid_user_home_dir_config_file(self):
        config = Config("kafka-rabbitmq-python.ini")
        self.assertIsInstance(config, Config)

    def test_success_get_section_key(self):
        config = Config("test.ini")
        expected = "http://localhost:5672"
        actual = config.get("RabbitMQ", "url")
        self.assertEqual(expected, actual)

    def test_fail_get_section_key_not_found_section(self):
        config = Config("test.ini")
        self.assertRaises(ValueError,
                          lambda: config.get("NotFound", "url"))

    def test_fail_get_section_key_not_found_key(self):
        config = Config("test.ini")
        self.assertRaises(ValueError,
                          lambda: config.get("RabbitMQ", "notfound"))
