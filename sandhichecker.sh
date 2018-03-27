#!/bin/bash

# This file is part of Tamil Sandhi Checker
# (C) 2018 Ezhil Language Foundation

if [ $# -le 0 ]; then
    echo "use from command line as : $ sandhichecker.sh <inputfile> <outputfile>"
    exit -1
fi
python -m tamilsandhi $@
