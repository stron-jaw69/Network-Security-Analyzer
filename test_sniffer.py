from scapy.all import sniff

# Simple sniff test that prints a summary for each captured packet
def handler(pkt):
    print("Captured:", pkt.summary())

sniff(count=5, prn=handler)
