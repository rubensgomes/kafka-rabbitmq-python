# -*- coding: utf-8 -*-
"""A class module that implements a simple RabbitMQ Producer.

This module provides the Producer class which is used to publish a
message to RabbitMQ message broker.

Typical usage example:

  from rubens_gomes.rabbitmq.producer import Producer

  publisher = Producer()
  publisher.publish("http://localhost:5672", "hello world")

@author: Rubens Gomes
"""
import pika
import string_utils

from rubens_gomes.common.exception import IllegalArgumentException


DEFAULT_EXCHANGE = "kafka-rabbitmq-exchange"
DEFAULT_QUEUE = "kafka-rabbitmq-queue"


class Producer(object):
    """A class responsible for publishing a message to RabbitMQ.
    """

    def __init__(self):
        """Initialize an instance of Producer.
        """

    def publish(self, url: str, body: str, exchange: str = DEFAULT_EXCHANGE):
        """Publishes the given body message to a RabbitMQ exchange.

        Parameters:
        ----------
        url: str
            The end point HTTP address of the RabbitMQ server.
        body: str
            The string object message to publish.
        exchange: str
            The name of RabgbitMQ exchange to publish the message to.  If not
            provide it defaults to the "default" exchange.

        Raises:
        -------
        rubens_gomes.common.exception.IllegalArgumentException
            If the url or body is empty.
        """
        if not string_utils.is_full_string(url):
            raise IllegalArgumentException(
                "Invalid url: " + url)

        if not string_utils.is_full_string(body):
            raise IllegalArgumentException(
                "Invalid body: " + body)

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
