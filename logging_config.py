#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018 Jun.

@author: huanglipang

logging config doc:
https://docs.python.org/2/library/logging.config.html
"""
import logging
import datetime
import time

class UTCFormatter(logging.Formatter):
    converter = time.gmtime


class RotatingFileNameHandler(logging.handlers.RotatingFileHandler):
    def __init__(self, filename, logPath):

        # set format type
        formatter = logging.Formatter(fmt="%(asctime)s - PID: %(process)d"\
                                        " - %(levelname)s - %(filename)s - %(message)s",
                                      datefmt="%Y-%m-%d %I:%M:%S %p")

        # set filename by the name of scripts
        logPath = logPath + "/" + filename.split('.')[0] + ".log"

        # please set the maxBytes by yourself
        # it will backup three files and delete the oldest one when create a new one
        super(RotatingFileNameHandler, self).__init__(filename=logPath, maxBytes=1024, backupCount=3)
        super(RotatingFileNameHandler, self).setFormatter(fmt=formatter)

        # NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
        super(RotatingFileNameHandler, self).setLevel(logging.INFO)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        # local time
        "standard": { 
            "format": "%(asctime)s - %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p"
        },
        "complete": {
            "format": "%(asctime)s - PID: %(process)d"\
                      " - %(levelname)s - %(filename)s - %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p"
        },
        "utc": {
            # "()" is a special key, which indicates a custom instantiation.
            "()": UTCFormatter,
            "format": "%(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p"
        }
    },
    "handlers": {
        # StreamHandler will show log in console
        "default": { 
            "level": "INFO",
            "formatter": "complete",
            "class": "logging.StreamHandler"
        }
    },
    # root logger
    "root": {
        "handlers": ["default"],
        "level": "INFO",
        "propagate": True
    }
}