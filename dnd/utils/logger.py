#!
# -*- coding: utf-8 -*-
"""
Created on 2020-12-18
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

import os
import logging
import tempfile

from logging.handlers import RotatingFileHandler


class WhitespaceRemovingFormatter(logging.Formatter):
    def format(self, record):
        record.msg = record.msg.strip()
        return super(WhitespaceRemovingFormatter, self).format(record)


logging.basicConfig(level=logging.DEBUG)
formatter = WhitespaceRemovingFormatter(
    "%(asctime)s.%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    "%Y-%m-%d %H:%M:%S",
)

tempdir = tempfile.gettempdir()
logfile = os.path.join(tempdir, "arc.log")

logfile = RotatingFileHandler(
    logfile,
    maxBytes=10000000,
    backupCount=5,
)
logfile.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(logfile)


if __name__ == "__main__":
    pass
