from utils.ping import ping_host
import sys

def main():

    hosts = ["127.0.0.1", "8.8.8.8"]
    other_hosts = sys.argv[1:]

    if other_hosts:
        hosts = hosts + other_hosts

    for host in hosts:
        ping_host(host)

if __name__ == "__main__":
    main()