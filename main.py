from utils.ping import ping_results, grade_connection
from utils.get_ip_addrs import get_default_gateway_ip, get_loopback_ip
from utils.responses import get_grade_response
from utils.net_test import test_connections
import sys

def main():
    print("\n================================================")
    print(" NETWORK HEALTH CHECK")
    print("================================================")

    # Get the IP addresses for the loopback and default gateway
    default_gateway_ip = get_default_gateway_ip()
    loopback_ip = get_loopback_ip()
    default_hosts = [loopback_ip, default_gateway_ip,"8.8.8.8"]

    # Get hosts from command-line arguments
    other_hosts = sys.argv[1:]

    # Test default hosts
    test_connections(default_hosts, True)

    # Test additional hosts if any
    if other_hosts:
        test_connections(other_hosts, False)

if __name__ == "__main__":
    main()