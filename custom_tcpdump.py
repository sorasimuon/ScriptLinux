#!/usr/bin/python

from optparse import OptionParser
from check_tcp_traffic import *

parser = OptionParser()

parser.add_option("-d", "--destination",
                  dest="destination",
                  help="define the packet IP destination")

parser.add_option("-s", "--source",
                  dest="source",
                  help="Define the packet IP source")
parser.add_option("-c", "--count",
                  dest="nb_pk",
                  type=int,
                  default=20,
                  help="Define the number of packets to collect")
parser.add_option("-p", "--port",
                  dest="port",
                  type=int,
                  help="Define the port to listen")
parser.add_option("-i", "--interface",
                  dest="interface",
                  help="Define the network interface to analyze")

(options, args) = parser.parse_args()

run_write_tcp_traffic(options)

