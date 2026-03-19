import subprocess
import platform

def get_ping_flag():
    os_name = platform.system().lower()

    if os_name == "windows":
        return "-n"
    else:
        return "-c"
    
def ping_host(host):
    flag = get_ping_flag()

    command = ["ping", flag, "4", host]
    print(f"Testing connection to {host} \nOne moment please.\n")
    result = subprocess.run(command, capture_output=True, text=True)

    return result.stdout