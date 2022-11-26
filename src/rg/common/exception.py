"""This module defines various exception types.

@author: Rubens Gomes
"""

__all__ = [
    "Error",
    "IllegalArgumentException",
    "ConfigurationException",
]


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class IllegalArgumentException (Error):
    """Exception raised when an expected function argument is missing or 
    when the argument has an invalid value.
    """

    def __init__(self, msg: str):
        """Initializes IllegalArgumentException with error message.

        Parameters:
        ----------
        msg: str
            explanation of the error
        """
        self.msg = msg


class ConfigurationException (Error):
    """Exception raised when a property is missing or is invalid in the
    configuration file.
    """

    def __init__(self, msg: str):
        """Initializes ConfigurationException with error message.

        Parameters:
        ----------
        msg: str
            explanation of the error
        """
        self.msg = msg


if __name__ == '__main__':
    pass
