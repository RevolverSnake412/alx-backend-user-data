#!/usr/bin/env python3
"""
filtered_logger.py
"""
from typing import List
import mysql.connector
import logging
import os
import re


FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def __init__(self, fields: List[str]):
    """
    Init
    """
    super(RedactingFormatter, self).__init__(self.format)
    self.fields = fields


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    formatter class
    """
    format = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    sc = ";"
    redaction = "***"

    def format(self, record: logging.LogRecord) -> str:
        """
        format
        """
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.redaction,
                                message, self.sc)
        return redacted


def get_logger() -> logging.Logger:
    """
    returns logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()

    formatter = RedactingFormatter(FIELDS)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    returns connect
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    pw = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    connect = mysql.connector.connect(user=user,
                                      password=pw,
                                      host=host,
                                      database=database)
    return connect


def main():
    """
    main function
    """
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    for row in cursor:
        message = "".join("{}={}; ".format(k, v) for k, v in zip(fields, row))
        logger.info(message.strip())
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
