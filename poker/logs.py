#!/usr/bin/env python
#
# Copyright (c) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = \
    ['\033[1;3%sm' % i for i in range(8)]
RESET = '\033[0m'

LOG_LEVELS = {
    'NOTSET': logging.NOTSET,
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}

LOG_LEVEL_COLORS = {
    'DEBUG': BLUE,
    'INFO': GREEN,
    'WARNING': YELLOW,
    'ERROR': RED,
    'CRITICAL': MAGENTA,
}


def set_logging_options(color=True, log_format=LOG_FORMAT, log_level='INFO',
                        filename=""):
    """Make the logging output pretty.

    :param color: if True, give different colors to the log level names
    :param log_format: string with logging format, see docs of logging module
    :param level: what level (and higher) of messages will be logged
    :param filename: if set, put the logging output into the file
    """
    if color:
        for level, color in LOG_LEVEL_COLORS.items():
            logging.addLevelName(LOG_LEVELS[level], color + level + RESET)
    if filename:
        logging.basicConfig(filename=filename,
                            level=LOG_LEVELS[log_level], format=log_format)
    else:
        logging.basicConfig(level=LOG_LEVELS[log_level], format=log_format)
