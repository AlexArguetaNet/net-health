from utils.ping import ping_results, grade_connection
from utils.get_ip_addrs import get_default_gateway_ip, get_loopback_ip
from utils.responses import get_grade_response
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

    # Test loopback address
    loopback_grade = grade_connection(*ping_results(loopback_ip))
    loopback_analysis = get_grade_response(loopback_grade, 1)

    print(loopback_analysis)


if __name__ == "__main__":
    main()