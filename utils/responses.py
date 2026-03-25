loopback_responses = {
    "FAILED": ["Internal Network Error", "Your device's communication system isn't responding. Your network card might be down."],
    "POOR": ["Internal Lag Detected", "Your device is struggling to process local data. Check for High CPU usage or memory leaks"],
    "FAIR": ["Local Loopback is Stable", "Responsiveness is lower than expected. Device may be using too many system resources."],
    "GOOD": ["Internal Systems are Healthy", "The internal network stack is functioning normally"],
    "EXCELLENT": ["Localhost is Perfect", "Internal data routing is working as excpected."]
}

dg_responses = {
    "FAILED": ["Gateway Unreachable", "You're disconnected from your local network. Check if your WI-FI is on or the ethernet cable is plugged in"],
    "POOR": ["Weak Signal to your Router", "You might experience frequent drops in signal. Try moving closer the WI-FI router or check for physical interference."],
    "FAIR": ["Network Response is Slow", "Local response from your router is slow. Try restarting your router. There may be too many devices connected."],
    "GOOD": ["Stable Connection", "Your internet router is working as expected"],
    "EXCELLENT": ["Strong Connection to your Router", "Local latency is minimal. Any slowdowns is likely ISP-related"]
}

open_web_responses = {
    "FAILED": ["No Internet access", "The web is unreacable. Your ISP or outside line is down."],
    "POOR": ["High Latency", "The internet is responding, but expect heavy lag caused by potential network congestion."],
    "FAIR": ["Slow Connection", "High definition video might buffer more"],
    "GOOD": ["Stable Internet", "Typical healthy connection for streaming and browsing"],
    "EXCELLENT": ["Fast internet Connection", "Your connection is blazing fast. Optimal for gaming and 4k video calls."]
}

generic_responses = {
    "FAILED": ["Host Unreachable", "The specific server is down or DNS lookup failed."],
    "POOR": ["Poor Connection to host", "The host is taking too long to respond. The serve might be very busy"],
    "FAIR": ["Slow Response", "The host is responding slowely. This connection might be experiencing path congestion."],
    "GOOD": ["Healthy Connection", "Host is responding normally."],
    "EXCELLENT": ["Fast Connection", "Host is responding instantly. You have a direct and fast connection to this host."]
}

def get_grade_response(results, id):
    if id == 0:
        responses = loopback_responses
    elif id == 1:
        responses = dg_responses
    elif id == 2:
        responses = open_web_responses
    else:
        responses = generic_responses

    return results[0], results[1], responses[results[1]]