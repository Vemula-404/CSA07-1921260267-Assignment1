import math
def nyquist(bw, levels):
    return 2 * bw * math.log2(levels)

if __name__ == "__main__":
    print(f"4-level, 3.1kHz: {nyquist(3100, 4)/1000:.1f} kbps")