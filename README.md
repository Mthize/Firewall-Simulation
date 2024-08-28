# Firewall Simulation

## Overview

This project simulates a basic firewall using Python and `scapy`, along with a Flask server and a client script for automated data collection and submission. It monitors network traffic, blocks IP addresses based on predefined rules, and logs events. The simulation also includes functionalities for generating random IPs and checking firewall rules.

## Features

- **Whitelist and Blacklist**: IP addresses can be specified in `whitelist.txt` and `blacklist.txt`.
- **Nimda Worm Detection**: Identifies and blocks traffic that matches the Nimda worm signature.
- **Traffic Monitoring**: Tracks packet rates and blocks IP addresses that exceed a specified threshold.
- **Logging**: Logs events in a timestamped log file for monitoring and debugging.
- **Random IP Generation**: Generates random IP addresses for testing purposes.
- **Firewall Rule Checking**: Checks whether a given IP address should be blocked based on predefined rules.
- **Flask Web Server**: A simple server that receives and saves system information.
- **Client Script**: Collects system information and sends it to the Flask server.

## Requirements

- Python 3.x
- `scapy` library
- `flask` library
- `requests` library
- Root privileges (required for modifying firewall rules)

## Installation

1. **Install Python 3**: Ensure that Python 3 is installed on your system.
2. **Install Required Libraries**: Install the necessary Python libraries using pip:
   ```bash
   pip install scapy flask requests




Usage
- 1. Firewall Simulation
- Prepare Configuration Files:

- Create a file named whitelist.txt and add IP addresses to be whitelisted (one per line).
- Create a file named blacklist.txt and add IP addresses to be blacklisted (one per line).
- Run the Firewall Simulation Script:

- Execute the script with root privileges to allow it to modify firewall rules:

 `sudo python firewall_simulation.py`

- The script will start monitoring network traffic. It will block IP addresses based on the rules defined and log events in the logs directory.

- 2. Random IP Generator and Firewall Rule Checker
- Run the Random IP Generator and Rule Checker Script:
- Execute the script to generate random IP addresses and check them against predefined firewall rules:

 `python random_ip_checker.py`

- 3. Flask Web Server
- Run the Flask Server:
- Execute the Flask server script:

 `python flask_server.py`

 - The server will run on port 3000 and listen for POST requests containing system information.

- 4. Client Script
- Run the Client Script:
- Execute the client script to collect system information and send it to the Flask server:

 `python client_script.py`

 - The script will repeatedly send system information to the server until a successful response is received.

- Example Log Entries
- Blocking blacklisted IP: 192.168.1.100
- Blocking Nimda source IP: 192.168.1.101
- Blocking IP: 192.168.1.102, packet rate: 50
  
- Notes
- Root Privileges: The firewall simulation script must be run with root privileges due to the need to modify iptables rules.
- Testing: Make sure to test in a controlled environment to avoid accidentally blocking legitimate traffic.
- Flask Server: Ensure the Flask server is running before executing the client script.

