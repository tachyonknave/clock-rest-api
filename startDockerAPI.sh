#!/bin/sh

source venv/bin/activate

# Clock URL should start with http:// or https://
# for example http://127.0.0.1

python3 clockAPI.py -a $CLOCK_URL