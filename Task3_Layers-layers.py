LAYERS = [("Application", "APP"), ("Transport", "TCP"),
          ("Network", "IP"), ("Data link", "ETH")]

def send(message):
    pdu = message
    for layer, tag in LAYERS:
        head = "[" + tag + "]"
        tail = "[FCS]" if tag == "ETH" else ""
        pdu = head + pdu + tail
        print(f"{layer:<12} adds {tag:<4} -> {len(pdu)} bytes")
    return pdu

if __name__ == "__main__":
    for msg in ["A" * 12, "A" * 1400]:
        print(f"\nMessage of {len(msg)} bytes")
        pdu = send(msg)
        overhead = len(pdu) - len(msg)
        print(f"Overhead = {overhead} B = {overhead / len(pdu) * 100:.2f}%")