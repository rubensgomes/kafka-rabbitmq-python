'''

Created on Nov 24, 2022
@author: Rubens Gomes
'''


class Producer(object):
    '''
    A simple RabbitMQ producer.
    '''

    # the RabbitMQ URL defined in application.ini properties file
    _rabbitmq_url = None

    def __init__(self):
        """Constructor to initialize an object instance of this type

        :param self: refers to any object instance of this type
        """
