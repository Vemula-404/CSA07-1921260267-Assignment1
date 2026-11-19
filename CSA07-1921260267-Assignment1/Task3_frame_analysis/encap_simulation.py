LAYERS = [
    ("Application", "APP"),
    ("Transport", "TCP"),
    ("Network", "IP"),
    ("Data link", "ETH")
]

def send(message):
    pdu = message
    for layer, tag in LAYERS:
        head = "[ " + tag + " ]"
        tail = "[FCS]" if tag == "ETH" else ""
        pdu = head + pdu + tail
        print(f"{layer:<12} adds {tag:<4} -> {len(pdu)} bytes")
    return pdu

if __name__ == "__main__":
    print("--- 12 Byte Message ---")
    send("A" * 12)
    print("\n--- 1,400 Byte Message ---")
    send("A" * 1400)