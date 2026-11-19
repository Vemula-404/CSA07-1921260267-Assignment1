def checksum(words):
    total = sum(words)
    while total > 0xFFFF:
        total = (total & 0xFFFF) + (total >> 16)
    return ~total & 0xFFFF

if __name__ == "__main__":
    words = [0x4500, 0x0073, 0x0000, 0x4000]
    cs = checksum(words)
    print(f"Checksum: {cs:04X}")