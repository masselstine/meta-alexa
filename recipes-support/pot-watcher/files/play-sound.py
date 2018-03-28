#!/usr/bin/python3

import pexpect

pexpect.run("ssh 192.168.42.1 'aplay /root/beedoo.wav'", events={'(?i)password':'incendia\n'})
