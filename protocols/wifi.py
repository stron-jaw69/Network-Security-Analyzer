# protocols/wifi.py
import struct

def parse_radiotap_header(data: bytes):
    if len(data) < 8:
        return None
    version, pad, length = struct.unpack("<BBH", data[:4])
    return {
        "rt_version": version,
        "rt_length": length,
        "raw_header": data[:length]
    }
def parse_80211_frame(data: bytes):
    if len(data) < 24:
        return None
    frame_control, duration = struct.unpack("<HH", data[:4])
    addr1 = data[4:10].hex(":")
    addr2 = data[10:16].hex(":")
    addr3 = data[16:22].hex(":")

    return {
        "frame_control": frame_control,
        "duration": duration,
        "addr1": addr1,
        "addr2": addr2,
        "addr3": addr3
    }