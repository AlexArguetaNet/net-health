import netifaces

def get_default_gateway_ip():

    try:
        default_gateway = netifaces.default_gateway()
        default_gateway_ip = default_gateway[netifaces.InterfaceType.AF_INET][0]

        return default_gateway_ip
    
    except Exception as e: # Default gateway interface not present on this computer
        return None

def get_loopback_ip():

    interface = ""

    # Get the loopback interface lo or lo0
    for i in netifaces.interfaces():
        if i == "lo" or i == "lo0":
            interface = i
            break
    
    if interface == "": # Loopback interface not on this computer
        return None
    else:
        # Extract loopback IP address
        interface_addresses = netifaces.ifaddresses(interface)
        loopback_ip = interface_addresses[netifaces.AF_INET][0]["addr"]

        return loopback_ip


