# -*- coding: utf-8 -*-
"""A class module that implements a simple RabbitMQ Producer.

This module provides the Producer class which is used to publish a
message to RabbitMQ message broker.

Typical usage example:

  from rubens_gomes.rabbitmq.producer import Producer

  pub = Producer()

@author: Rubens Gomes
"""
import pika

from rubens_gomes.common.config import Config


DEFAULT_EXCHANGE = "kafka-rabbitmq-exchange"
DEFAULT_QUEUE = "kafka-rabbitmq-queue"


class Producer(object):
    """A class responsible for publishing a message to RabbitMQ.
    """

    def __init__(self):
        """Initialize an instance of Producer.
        """
        self.config = Config()

    def publish_msg(self, exchange: str = DEFAULT_EXCHANGE, body: str):
        """Publishes the given body message to a RabbitMQ exchange.

        Parameters:
        ----------
        exchange: str
            The name of RabgbitMQ exchange to publish the message to.  If not
            provide it defaults to the "default" exchange.
        body: str
            The string object message to publish.

        Raises:
        -------
        rubens_gomes.common.exception.IllegalArgumentException
            If the body is empty.
        """
        url = self.config.get("RabbitMQ", "url")
        # connect to RabbitMQ broker
        connection = pika.BlockingConnection(pika.ConnectionParameters(url))
        channel = connection.channel()
        # ensure a RabbitMQ queue is created
        channel.queue_declare(queue=DEFAULT_QUEUE)
        # submit message to that queue exchange
        channel.basic_publish(exchange=DEFAULT_EXCHANGE,
                              body=body)
        # close connection
        connection.close()
