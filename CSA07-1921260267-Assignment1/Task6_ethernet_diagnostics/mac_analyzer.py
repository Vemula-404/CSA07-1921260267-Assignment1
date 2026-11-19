def analyze_mac(mac):
    first_byte = int(mac.split(':')[0], 16)
    is_multicast = (first_byte & 0x01) == 1
    print(f"MAC: {mac}")
    if is_multicast:
        print("Type: Multicast (Group)")
    else:
        oui = ":".join(mac.split(':')[:3])
        print(f"Type: Unicast. OUI: {oui}")

if __name__ == "__main__":
    analyze_mac("01:00:5e:0a:01:02")
    analyze_mac("3c:52:82:11:22:33")