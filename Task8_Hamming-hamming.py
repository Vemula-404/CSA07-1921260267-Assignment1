def encode(d):
    # d = [d1, d2, d3, d4]; positions 1..7 = p1 p2 d1 p3 d2 d3 d4
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]

def decode(c):
    c = c[:]
    s1 = c[0] ^ c[2] ^ c[4] ^ c[6]
    s2 = c[1] ^ c[2] ^ c[5] ^ c[6]
    s3 = c[3] ^ c[4] ^ c[5] ^ c[6]
    pos = s1 + 2 * s2 + 4 * s3
    if pos != 0:
        c[pos - 1] ^= 1
    return pos, [c[2], c[4], c[5], c[6]]

if __name__ == "__main__":
    cw = encode([1, 0, 1, 1])
    print("codeword", "".join(map(str, cw)))
    pos, data = decode(cw)
    print("no error: syndrome", pos, "data", "".join(map(str, data)))
    bad = cw[:]; bad[4] ^= 1
    pos, data = decode(bad)
    print("error at", pos, "-> data", "".join(map(str, data)))
    rx = [0, 1, 1, 0, 1, 1, 1]
    pos, data = decode(rx)
    print("Task 8.3 received 0110111: error at", pos, "data", "".join(map(str, data)))
    two = cw[:]; two[2] ^= 1; two[4] ^= 1
    pos, data = decode(two)
    print("2-bit error (bits 3,5): syndrome", pos, "data", "".join(map(str, data)), "(WRONG)")