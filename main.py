from utils.ping import ping_ip
import sys

def main():

    ip_addresses = ["127.0.0.1", "8.8.8.8"]
    other_ip = sys.argv[1:]

    if other_ip:
        ip_addresses = ip_addresses + other_ip

    for ip in ip_addresses:
        ping_ip(ip)

if __name__ == "__main__":
    main()