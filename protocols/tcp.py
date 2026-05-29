# protocols/tcp.py
import struct

def parse_tcp_segment(data: bytes):
    if len(data) < 20:
        return None
    (src_port, dst_port, seq, ack, offset_reserved_flags) = struct.unpack('!HHLLH', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flags = offset_reserved_flags & 0x01FF
    return {
        "src_port": src_port,
        "dst_port": dst_port,
        "seq": seq,
        "ack": ack,
        "flags": flags,
        "header_len": offset,
        "payload": data[offset:]
    }
