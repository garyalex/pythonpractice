"""Term output functions."""

import datetime
from blessings import Terminal


class TermOutput(object):
    """A terminal object for outputing formatted messages."""

    def __init__(self):
        """Return a TermOutput object."""

    def output(self, message, level="info"):
        """Print a message in the info format."""
        t = Terminal()
        if len(message) == 0:
            raise RuntimeError("No message supplied")
        # Get timestamp
        timestamp = t.white("{:%Y-%m-%d %H:%M:%S} ".format(datetime.datetime.now()))
        # Check level
        if level == "debug":
            prefix = t.blue("DEBUG: ")
        elif level == "info":
            prefix = t.green("INFO:  ")
        elif level == "warn":
            prefix = t.yellow("WARN:  ")
        elif level == "error":
            prefix = t.red("ERROR: ")
        else:
            raise RuntimeError("That level is not supported!")
        # Combine timestamp, refix and message
        print(timestamp + prefix + message)
        return
