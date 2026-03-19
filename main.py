from utils.ping import ping_host
from utils.get_ip_addrs import get_default_gateway_ip, get_loopback_ip
import sys

def main():

    default_gateway_ip = get_default_gateway_ip()
    loopback_ip = get_loopback_ip()

    #These hosts will be tested by default
    hosts = [loopback_ip, default_gateway_ip,"8.8.8.8"]

    # Other hosts entered as command-line arguments
    other_hosts = sys.argv[1:]

    if other_hosts:
        hosts = hosts + other_hosts

    for host in hosts:
        print(ping_host(host))



if __name__ == "__main__":
    main()