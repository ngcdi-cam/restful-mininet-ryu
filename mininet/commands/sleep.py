import time

from mininet.cli import CLI

def sleep(self, line):
    args = line.split()
    assert len(args) == 1
    time.sleep(float(args[0]))

CLI.do_sleep = sleep
