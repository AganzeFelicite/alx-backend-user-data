#!/usr/bin/env python3
"""
this is a function that returns
a log on the screen
"""
from typing import List
import logging
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    for item in fields:
        message = re.sub(rf"{item}=(.*?)\{separator}",
                         f"{item}={redaction}{separator}", message)
    return message
