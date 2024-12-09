import argparse
import socket
import platform
import subprocess
from colorama import init, Fore

# Initialize colorama
init()

def get_host_info(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "Unknown"

    return {
        "IP Address": ip,
        "Hostname": hostname,
        "System Info": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
    }

def get_mac_address(ip):
    try:
        if platform.system() == "Windows":
            result = subprocess.check_output(["arp", "-a"], encoding="utf-8")
        else:
            result = subprocess.check_output(["arp", "-n"], encoding="utf-8")

        lines = result.splitlines()
        for line in lines:
            if ip in line:
                mac_address = line.split()[-2] if platform.system() == "Windows" else line.split()[2]
                return mac_address
    except Exception:
        return "MAC Address not found"
    return "MAC Address not found"

def display_info(info, mac_address):
    # Updated ASCII art
    ascii_art = """
    ███╗   ███╗ █████╗ ██╗   ██╗██╗      ██████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗
    ████╗ ████║██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
    ██╔████╔██║███████║ ╚████╔╝ ██║     ██║   ██║█████╗██║   ██████╔╝███████║██║     █████╔╝ 
    ██║╚██╔╝██║██╔══██║  ╚██╔╝  ██║     ██║   ██║╚════╝██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
    ██║ ╚═╝ ██║██║  ██║   ██║   ███████╗╚██████╔╝      ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """
    
    # Display ASCII art (no color change here)
    print(ascii_art)
    
    # Now display other info in green
    print(Fore.GREEN + "=== Maylo-Track ===")
    for key, value in info.items():
        print(Fore.GREEN + f"{key}: {value}")
    print(Fore.GREEN + f"MAC Address: {mac_address}")

def main():
    parser = argparse.ArgumentParser(description="Maylo-Track: Local IP Tracking Tool")
    parser.add_argument("ip", help="IP address to track")
    args = parser.parse_args()
    
    ip = args.ip
    info = get_host_info(ip)
    mac_address = get_mac_address(ip)
    display_info(info, mac_address)

if __name__ == "__main__":
    main()
