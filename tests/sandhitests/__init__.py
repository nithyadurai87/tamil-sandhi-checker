# This file is part of Tamil Sandhi Checker project

import sys
import os
import unittest

sandhi_test_path = (os.sep).join(os.getcwd().split(os.sep)[:-1])
sys.path.insert(0,sandhi_test_path)

PYTHON2_7 = (sys.version[0:3] == '2.7')
PYTHON2_6 = (sys.version[0:3] == '2.6')
PYTHON3 = sys.version > '3'
WINDOWS = (sys.platform.find('win') != -1)
LINUX = not WINDOWS

import tamil
from tamilsandhi.sandhi_checker import *

