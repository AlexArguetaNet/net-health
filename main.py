from utils.ping import ping_results, grade_connection
from utils.get_ip_addrs import get_default_gateway_ip, get_loopback_ip
from utils.responses import get_grade_response
import sys

def main():
    print("Net Health Test in Progress\n")

    default_gateway_ip = get_default_gateway_ip()
    loopback_ip = get_loopback_ip()

    #These hosts will be tested by default
    default_hosts = [loopback_ip, default_gateway_ip,"8.8.8.8"]

    # Get grade responses from the default hosts
    responses = []

    for i in range(len(default_hosts)):
        grade = grade_connection(*ping_results(default_hosts[i]))
        responses.append(get_grade_response(grade, i))

    # Other hosts entered as command-line arguments
    other_hosts = sys.argv[1:]
    other_responses = []

    if other_hosts:
        for host in other_hosts:
            grade = grade_connection(*ping_results(host))
            other_responses.append(get_grade_response(grade, 3))    

    # Display test responses for default hosts
    print("Results\n")

    print(f"Localhost: {responses[0][1]}")
    print(responses[0][2][1])
    print("\n")

    print(f"Router: {responses[1][1]}")
    print(responses[1][2][1])
    print("\n")

    print(f"Internet Access: {responses[2][1]}")
    print(responses[2][2][1])
    print("\n")

    # Display test responses for additional hosts
    for i in range(len(other_hosts)):
        print(f"{other_hosts[i]}: {other_responses[0][1]}")
        print(other_responses[i][2][1])
        print("\n")
    

        


if __name__ == "__main__":
    main()