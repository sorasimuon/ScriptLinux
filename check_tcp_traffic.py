from subprocess import Popen, PIPE
from datetime import datetime
import dpkt


def run_write_tcp_traffic(options):
    '''
    This function is used to check the TCP/UDP Traffic occuring on the current machine
    :param options:
    :return: create a pcap file ready for analysis
    '''

    dest = options.destination
    source = options.sources
    nb_pk = options.nb_pk
    port = options.port
    interface = options.interface


    p = Popen("tcpdump -i {} -t -c {} -w {} \"port {}\"".format(interface, nb_pk, "$HOME/Logs/tcp_traffic_-_{}.pcap".format(datetime.now().strftime("%Y%m%d_-_%H%M%S")), port), shelll=True)

if __name__ == "__main__":

    run_write_tcp_traffic()
