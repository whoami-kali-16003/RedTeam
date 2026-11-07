# Day 4 Condition & Operators
a = int (input("Enter a 1st Number: "))
b = int (input("Enter a 2nd Number: "))
print(f"a = {a}, b = {b}")
print(f"Addition (a+b): {a+b}")
print(f"Comparison (a > b): {a > b}")
print(f"Logical (a > 5 and b < 5): {a > 5 and b < 5}")

print("\n--- Simple if-else (Simple Example)")
# Example 1: Port Checker
port = int(input("Enter a port number to check: "))

if port == 22:
    print(f"Port {port} is for SSH - Secure Shell")
elif port == 80:
    print(f"Port {port} is for HTTP - Web Server")
elif port == 443:
    print(f"Port {port} is for HTTPS - Secure Web Server")
else:
    print(f"Port {port} is not a common port")

print("\n--- Login Simulation ---")
password = input("Enter password to access tool: ")

if password == "admin123":
    print("Access Granted! Welcome!")
else:
    print("Access Denied! Wrong Password!")
