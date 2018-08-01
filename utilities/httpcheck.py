#!/usr/bin/env python3
"""Check for http connection and status."""

import requests
import argparse
import time
import sys
import validators
import termoutput

# Setup our arguments
parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="URL to check",
                    required=True, type=str)
parser.add_argument("--interval", "-i",
                    help="Time between checks", type=int, default=30)
parser.add_argument("--count", "-c", help="Number of checks",
                    type=int, default=5)
parser.add_argument("--debug", "-d", action="store_true", help="verbose flag")
args = parser.parse_args()

# Set our variables from commandline arguments
check_url = args.url
check_int = args.interval
check_count = args.count
debug = args.debug

# Setup our terminal
term = termoutput.TermOutput()

if debug:
    term.output("URL: %s" % check_url, level="debug")
    term.output("Check interval: %s" % check_int, level="debug")
    term.output("Check count: %s" % check_count, level="debug")

# Validate URL
if not validators.url(check_url):
    term.output("Error: URL invalid: %s" % check_url, level="error")
    sys.exit(1)

counter = 0

while counter < check_count:
    start = time.time()
    try:
        # r = requests.get(check_url, verify=False)
        r = requests.get(check_url)
    except requests.exceptions.ConnectionError:
        term.output("Conn error: %s" % check_url, level="warn")
    else:
        roundtrip = round(time.time() - start, 3)
        statCode = r.status_code
        term.output(
            "Conn success - Status: %s Response Time: %s secs" % (
                statCode, roundtrip)
        )
    try:
        term.output("Waiting %s secs before next attempt" % check_int)
        time.sleep(check_int)
    except KeyboardInterrupt:
        term.output("Exiting...")
        sys.exit(0)
    counter += 1
