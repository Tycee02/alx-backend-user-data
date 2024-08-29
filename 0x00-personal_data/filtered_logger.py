#!/usr/bin/env python3
"""
Regex-ing
"""

import re
import logging
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(
        fields: list[str], redaction: str, message: str, separator: str,
        ) -> str:
    """
    Returns the log message obfuscated
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
     """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in the log record
        """
        msg = super(RedactingFormatter, self).format(record)
        text = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return text


if __name__ == "__main__":
    main()
