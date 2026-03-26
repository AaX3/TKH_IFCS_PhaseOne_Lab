#!/usr/bin/env python3
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
# YOUR CODE HERE: 

import subprocess

# Running the command to list all processes
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)


# INSTRUCTION 2: Search the captured output for the malicious process
# YOUR CODE HERE

# Checking if the malicious process name is inside the output
if "unauthorized_cryptominer" in process_list.stdout:
    print("Threat detected!")

# INSTRUCTION 3: If found, create a dictionary and save it to 'security_alert.json'
# YOUR CODE HERE:

alert_data = {
        "event": "Unauthorized Process", 
        "severity": "High", 
        "process": "unauthorized_cryptominer"
    }
print("[+] Audit Complete.")

import json

# Open the file in write mode ("w")
with open("security_alert.json", "w") as file:
    json.dump(alert_data, file, indent=4)
