# Parse TCP segment headers and payload from raw packet bytes
import struct

def parse_tcp(data):
    if len(data) < 20:
        return None
    src, dst, seq, ack, off_flags = struct.unpack("!HHLLH", data[:14])
    offset = (off_flags >> 12) * 4
    flags = off_flags & 0x1FF
    return {
        "src_port": src,
        "dst_port": dst,
        "seq": seq,
        "ack": ack,
        "flags": flags,
        "header_len": offset,
        "payload": data[offset:]
    }

