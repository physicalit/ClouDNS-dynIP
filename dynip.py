#!/usr/bin/env python

####################################################
# License                                          #
# -------                                          #
# Copyright (c) 2015 physicalIT                    #
# The project is licensed under the MIT license.   #
####################################################

# Importing the config.py file
#=============================
from config import *

# Counting the lines of config.py file
# ====================================
num_lines = sum(1 for line in open('config.py'))
lines = num_lines - 11

# Importing the module to open the links
# ======================================
import urllib

# Creating the loop for opening the links one by one
# ==================================================
i = 0
while i < lines:               # The number on time the loob will repeat
    url_number = 100 + i
    page = urllib.urlopen(urls[url_number])
    page.close()
    i = i + 1
