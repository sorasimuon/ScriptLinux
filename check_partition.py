#!/usr/bin/python

import sys
import os

from optparse import OptionParser



parser = OptionParser()

parser.add_option("-t", "--threshold",
                  dest="threshold",
                  type=int,
                  default=75,
                  help="Set threshold level (%)")

parser.add_option("-s", "--singleshot",
                  dest="singleshot",
                  default=False,
                  action="store_true",
                  help="just check once, do not loop")

parser.add_option("-m", "--mailbox",
                  dest="mailbox",
                  help="mai report to this mailbox")

(options, partition_list) = parser.parse_args()

print("Threshold : {}".format(options.threshold))
print("Mailbox : {}".format(options.mailbox))
print("Singleshot : {}".format(options.singleshot))



