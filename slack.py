#!/usr/bin/env python3
"""Slack client for sending messages to myself."""

import os
import argparse
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

parser = argparse.ArgumentParser()
parser.add_argument("--message", "-m", help="Message to send", type=str,
                    required=True)
args = parser.parse_args()
message = args.message

sc.api_call(
    "chat.postMessage",
    channel="U48E0MGQP",
    asuser="false",
    username="slack.py",
    text=message,
)
