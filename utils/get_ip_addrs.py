import subprocess
import platform

os_name = platform.system().lower()

def get_default_gateway_ip():

    default_gateway_ip = None

    try:

        if os_name == "linux":

            result = subprocess.run(["ip", "route"], capture_output=True, text=True)
            output_list = result.stdout.split(" ")
            default_gateway_ip = output_list[2]
        
        elif os_name == "windows":

            result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        
        return default_gateway_ip

    except Exception as e:
        return None
    
def get_loopback_ip():

    loopback_ip = None
    
    try:
        
        if os_name == "linux":
            command = ["ip", "a", "show", "dev", "lo"]
            result = subprocess.run(command, capture_output=True, text=True)
            result = result.stdout.strip().split("\n")

            ip_line = result[2].strip()
            loopback_ip = ip_line.split()[1].split("/")[0]

        return loopback_ip
        

    except Exception as e:
        return None



