from utils.ping import ping_results, grade_connection
from utils.get_ip_addrs import get_default_gateway_ip, get_loopback_ip
from utils.responses import get_grade_response
from utils.net_test import test_connections, spinner
import sys
import threading
import time

def main():
    print("\n================================================")
    print(" NETWORK HEALTH CHECK")
    print("================================================")

    # Get the IP addresses for the loopback and default gateway
    default_gateway_ip = get_default_gateway_ip()
    loopback_ip = get_loopback_ip()
    default_hosts = [loopback_ip, default_gateway_ip,"8.8.8.8"]
    default_names = ["Localhost", "Router", "Internet"]
    other_hosts = sys.argv[1:]

    t = threading.Thread(target=spinner)
    t.daemon = True
    t.start()

    try:
        default_output = test_connections(default_hosts, True)
        if other_hosts:
            other_output = test_connections(other_hosts, False)
    finally:
        t.do_run = False
        t.join()

    print("CORE CONNECTIVITY:")
    id = 0
    for line in default_output:
        print(f"[ {line[0]:^4} ] {default_names[id]:<12} : {line[2]} ")
        id += 1

    if other_hosts:
        print("\nEXTERNAL HOSTS:")
        i = 0
        for line in other_output:
            print(f"[ {line[0]:^4} ] {other_hosts[i]:<12} : {line[2]} ")
            i += 1

    print("\n")
    

if __name__ == "__main__":
    main()