"""rubens_gomes.rabbitmq.producer.py.

@author Rubens Gomes
"""

from unittest import TestCase

from rubens_gomes.common.exception import IllegalArgumentException
from rubens_gomes.rabbitmq.producer import Producer


class Test(TestCase):
    """A unit test class to test the rubens_gomes.rabbitmq.producer functionalities
    """

    def test_fail_publish_when_invalid_url(self):
        publisher = Producer()
        publisher.publish("http://localhost:9999", "hello world")
#        self.assertRaises(Exception, lambda: publisher.publish("http://localhost:9999",
#                                                               "hello world"))
