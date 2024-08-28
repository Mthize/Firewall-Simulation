import sys
import time
from scapy.all import Ether, IP, TCP, sendp

TARGET_IP = "192.168.1.x"
INTERFACE = "eth0"
NUM_PACKETS = 100
DURATION = 5

def send_packets(target_ip, interface, num_packets, duration):
    packet = Ether() / IP(dst=target_ip) / TCP()
    end_time = time.time() + duration
    packet_count = 0

    while time.time() < end_time and packet_count < num_packets:
        sendp(packet, iface=interface, verbose=False)
        packet_count += 1

    print(f"Sent {packet_count} packets")

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("This script requires Python 3.")
        sys.exit(1)

    send_packets(TARGET_IP, INTERFACE, NUM_PACKETS, DURATION)