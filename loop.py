# Day 5 - Loops

print("--- 1. For Loop ---")
# Scanning a list of common ports
common_ports = [21, 22, 80, 443, 8080]
for port in common_ports:
    print(f"Checking port {port}...")

print("\n--- 2. Range with For Loop ---")
for i in range(1, 6):
    print(f"Attempt {i}")

print("\n--- 3. While Loop ---")
count = 3
while count > 0:
    print(f"Retrying... {count} chances left")
    count = count - 1

print("\n--- 4. Loop with Condition (Break) ---")
# Simple password check with 3 tries
correct_password = "admin123"
for attempt in range(1, 4):
    pwd = input(f"Attempt {attempt}/3 - Enter password: ")
    if pwd == correct_password:
        print("Access Granted!")
        break
    else:
        print("Wrong password!")
else:
    print("All attempts failed! Access Denied!")
