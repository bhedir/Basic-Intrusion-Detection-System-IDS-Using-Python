from scapy.all import *
import argparse
import logging
from collections import defaultdict

# Configuration des logs
logging.basicConfig(
    filename='anomalies.log',
    filemode='a',
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

packet_counter = defaultdict(int)
allowed_ports = [80, 443, 53, 22, 21]  # Add more allowed ports here if necessary

def log_anomaly(message):
    print(message)
    logging.info(message)

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet.sport if hasattr(packet, 'sport') else None
        dst_port = packet.dport if hasattr(packet, 'dport') else None
        protocol = packet.proto

        packet_counter[src_ip] += 1

        if packet_counter[src_ip] > 100:
            log_anomaly(f"[!] Trop de paquets venant de {src_ip}")

        if src_port and src_port not in allowed_ports:
            log_anomaly(f"[!] Port non autorisé {src_port} utilisé par {src_ip}")
        elif src_port and src_port in allowed_ports:
            log_anomaly(f"[+] Port autorisé {src_port} utilisé par {src_ip}")

        if dst_port and dst_port not in allowed_ports:
            log_anomaly(f"[!] Port non autorisé {dst_port} utilisé vers {dst_ip}")
        elif dst_port and dst_port in allowed_ports:
            log_anomaly(f"[+] Port autorisé {dst_port} utilisé vers {dst_ip}")

        print(f"Packet: {src_ip}:{src_port} → {dst_ip}:{dst_port} (proto {protocol})")


def live_capture():
    print("🔴 Capture en direct - Ctrl+C pour arrêter")
    sniff(prn=analyze_packet, store=0)

def analyze_pcap(file_path):
    print(f"📂 Analyse du fichier {file_path}")
    packets = rdpcap(file_path)
    for pkt in packets:
        analyze_packet(pkt)
    print("✅ Analyse terminée.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mini IDS - Analyse réseau")
    parser.add_argument("-f", "--file", help="Fichier .pcap à analyser")
    args = parser.parse_args()

    try:
        if args.file:
            analyze_pcap(args.file)
        else:
            live_capture()
    except KeyboardInterrupt:
        print("\nArrêt de l'analyse.")
        print("📄 Les anomalies ont été enregistrées dans anomalies.log")

