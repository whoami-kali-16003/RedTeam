# Day 6 - Functions

# 1. Simple Function
def banner():
    print("=== Red Team Tool ===")
    print("Author: Anonymous")
    print("=====================")

banner()

# 2. Function with Argument - Port Info Tool
def check_port(port):
    if port == 22:
        return "SSH - Secure Shell"
    elif port == 80:
        return "HTTP - Web Server"
    elif port == 443:
        return "HTTPS - Secure Web"
    else:
        return "Unknown Port"

print("\n--- Port Checker Tool ---")
p = int(input("Enter port number: "))
result = check_port(p)
print(f"Port {p} is: {result}")

# 3. Function with multiple arguments
def scan_target(ip, port):
    print(f"\nScanning {ip} on port {port}...")
    service = check_port(port)
    print(f"Found: {service} on {ip}")

# Using the function
scan_target("192.168.1.1", 22)
scan_target("192.168.1.1", 80)
