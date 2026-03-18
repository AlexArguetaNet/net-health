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
    print(f"Pinging {host}. One moment please.")
    result = subprocess.run(command, capture_output=True, text=True)

    print(result.stdout)

    return result.returncode