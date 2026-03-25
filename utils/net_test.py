from .ping import ping_results, grade_connection
from .responses import get_grade_response

def test_connections(hosts, is_default):
    if is_default:
        title = "CORE CONNECTIVITY:"
        names = ["Localhost", "Router", "Internet"]
    else:
        title = "EXTERNAL HOSTS:"
        names = hosts

    print(f"\n{title}")

    if is_default:
        id = 0
        for host in hosts:
            # Get connection grade
            grade = grade_connection(*ping_results(host))
            response = get_grade_response(grade, id)

            print(f"[{response[0]:^4}] {names[id]:<12} : {response[2]}")
            id += 1
    else:
        for i in range(len(hosts)):
            grade = grade_connection(*ping_results(hosts[i]))
            response = get_grade_response(grade, 3)
            print(f"[{response[0]:^4}] {hosts[i]:<12} : {response[2]}")




    
            