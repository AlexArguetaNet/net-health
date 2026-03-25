loopback_responses = {
    "FAILED": "Internal Network Error",
    "POOR": "Internal Lag Detected",
    "FAIR": "Local Loopback is Stable",
    "GOOD": "Internal Routing is Healthy",
    "EXCELLENT": "Internal Routing is Stable"
}

dg_responses = {
    "FAILED": "Gateway Unreachable",
    "POOR": "Weak Signal to your Router",
    "FAIR": "Network Response is Slow",
    "GOOD": "Stable Connection",
    "EXCELLENT": "Strong Connection to your Router"
}

open_web_responses = {
    "FAILED": "No Internet access",
    "POOR": "High Latency",
    "FAIR": "Slow Connection",
    "GOOD": "Stable Internet",
    "EXCELLENT": "Fast internet Connection"
}

generic_responses = {
    "FAILED": "Host Unreachable",
    "POOR": "Poor Connection to host",
    "FAIR": "Slow Response",
    "GOOD": "Healthy Connection",
    "EXCELLENT": "Fast Connection",
}

def get_grade_response(grade, id):
    if id == 0:
        responses = loopback_responses
    elif id == 1:
        responses = dg_responses
    elif id == 2:
        responses = open_web_responses
    else:
        responses = generic_responses

    return grade[0], grade[1], responses[grade[1]]