import subprocess
import platform

os_name = platform.system().lower()

def get_ping_flag():
    if os_name == "windows":
        return "-n"
    else:
        return "-c"
    
def ping_host(host):
    flag = get_ping_flag()

    command = ["ping", flag, "4", host]
    print(f"Testing connection to {host} \nOne moment please.\n")
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout.strip().split("\n")

    return result

def ping_stats(host):

    try:
        
        results = ping_host(host)

        if os_name == "windows":

            packets_line = []
            time_line = []

            for line in results:
                if "Packets" in line:
                    packets_line = line.strip().replace(" ", "").split(",")
                if "Minimum" in line:
                    time_line = line.strip().replace(" ", "").split(",")
            
            packet_lost = packets_line[2].split("=")[1][0]
            min_time = time_line[0].split("=")[1].split("m")[0]


        return [int(packet_lost), int(min_time)]




    except Exception as e:
        return None