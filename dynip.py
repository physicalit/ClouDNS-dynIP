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

# Importing the module to open the links
# ======================================
import urllib

# Creating the loop for opening the links one by one
# ==================================================
i = 0
while i < 3:               # The number on time the loob will repeat
    url_number = 100 + i
    page = urllib.urlopen(urls[url_number])
    page.close()
    i = i + 1
