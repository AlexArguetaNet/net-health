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

def ping_results(host):

    try:
        
        results = ping_host(host)
        packets_line = []
        time_line = []

        if os_name == "windows":
            for line in results:
                if "Packets" in line:
                    packets_line = line.strip().replace(" ", "").split(",")
                if "Minimum" in line:
                    time_line = line.strip().replace(" ", "").split(",")
            
            packet_loss = packets_line[2].split("=")[1][0]
            min_time = time_line[0].split("=")[1].split("m")[0]
            avg_latency = time_line[2].split("=")[1].split("m")[0]
            max_time = time_line[1].split("=")[1].split("m")[0]

        elif os_name == "linux":
            for line in results:
                if "packets" in line:
                    packets_line = line.strip().replace(" ", "").split(",")
                if "rtt" in line:
                    time_line = line.strip().replace(" ", "").split("=")
            
            packet_loss = packets_line[2][0]
            min_time = time_line[1].split("/")[0]
            avg_latency = time_line[1].split("/")[1]
            max_time = time_line[1].split("/")[2]

        return int(packet_loss), float(avg_latency), float(max_time) - float(min_time)

    except Exception as e:
        return None

def grade_connection(packet_loss, avg_latency, jitter):

    score = 100

    # Deduct for packet loss: 1% drops 20 points
    loss_penalty = packet_loss * 20
    score -= loss_penalty

    # Deduct for latency: 
    # Every 10ms after 50ms costs 1 point
    if avg_latency > 50:
        latency_penalty = (avg_latency - 50) / 10
        score -= latency_penalty

    # Deduct for jitter
    if jitter > 5:
        jitter_penalty = ((jitter - 5) / 5) * 5
        score -= jitter_penalty

    # Make sure the score is between 0 and 100
    score = max(0, min(100, score))

    # Assign description to grade
    description = ""

    if packet_loss >= 100:
        description = "FAILED"
    else:
        if score >= 90:
            description = "EXCELLENT"
        elif score >= 80:
            description = "GOOD"
        elif score >= 60:
            description = "FAIR"
        else:
            description = "POOR"
    
    return score, description


