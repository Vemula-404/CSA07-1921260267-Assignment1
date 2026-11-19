import math

def shannon(bw_hz, snr_db):
    snr = 10 ** (snr_db / 10)
    return bw_hz * math.log2(1 + snr)

if __name__ == "__main__":
    print(f"Cat6 (40dB, 250MHz): {shannon(250e6, 40)/1e6:.2f} Mbps")
    print(f"Near welders (15dB): {shannon(250e6, 15)/1e6:.2f} Mbps")
    print(f"Wi-Fi 6 (1.5dB):     {shannon(160e6, 15)/1e6:.2f} Mbps")