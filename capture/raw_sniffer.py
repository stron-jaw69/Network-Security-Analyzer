import socket
import struct
import time
from protocols.wifi import parse_radiotap_header, parse_80211_frame

# Create a raw packet socket to capture all frames on the interface
def create_raw_socket(interface=None):
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    if interface:
        s.bind((interface, 0))
    return s

def parse_eth(data):
    dest, src, proto = struct.unpack("!6s6sH", data[:14])
    return {
        "dest_mac": dest.hex(":"),
        "src_mac": src.hex(":"),
        "eth_proto": proto
    }

def sniff(interface):
    sock = create_raw_socket(interface)
    while True:
        raw, _ = sock.recvfrom(65535)
        # Detect Radiotap (802.11) frames
        if raw[0] == 0x00:  # Radiotap version 0
            rt = parse_radiotap_header(raw)
            wifi = parse_80211_frame(raw[rt["rt_length"]:])
            yield {
                "timestamp": time.time(),
                "raw": raw,
                "radiotap": rt,
                "wifi": wifi
            }
            continue

        # Fallback to Ethernet
        yield {
            "timestamp": time.time(),
            "raw": raw,
            "eth": parse_eth(raw)
        }