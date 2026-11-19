def hamming_reqs(m):
    r = 1
    while (2**r) < (m + r + 1):
        r += 1
    return r

if __name__ == "__main__":
    m = 16
    r = hamming_reqs(m)
    total = m + r
    print(f"Data bits: {m}, Check bits: {r}, Total: {total}")
    print(f"Overhead: {r/total*100:.1f}%")