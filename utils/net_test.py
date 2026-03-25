from .ping import ping_results, grade_connection
from .responses import get_grade_response
import threading
import time
import sys

def spinner():
    while getattr(threading.current_thread(), "do_run", True):
        for cursor in "|/-\\":
            sys.stdout.write(f"\rTesting... {cursor}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r                    \n")

def test_connections(hosts, is_default):

    responses = []

    if is_default:
        id = 0
        for host in hosts:
            # Get connection grade
            grade = grade_connection(*ping_results(host))
            responses.append(get_grade_response(grade, id))
            id += 1
    else:
        for i in range(len(hosts)):
            grade = grade_connection(*ping_results(hosts[i]))
            responses.append(get_grade_response(grade, 3))

    return responses







    
            