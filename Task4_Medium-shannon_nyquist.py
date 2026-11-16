import math

def nyquist(bandwidth_hz, levels):
    return 2 * bandwidth_hz * math.log2(levels)

def shannon(bandwidth_hz, snr_db):
    snr = 10 ** (snr_db / 10)
    return bandwidth_hz * math.log2(1 + snr)

if __name__ == "__main__":
    print(f"Telephone (3100 Hz, 30 dB): {shannon(3100, 30)/1e6:.2f} Mbps")
    print(f"Cat6 (250 MHz, 40 dB):      {shannon(250e6, 40)/1e6:.2f} Mbps")
    print(f"Cat6 near welders (15 dB):  {shannon(250e6, 15)/1e6:.2f} Mbps")
    print(f"Wi-Fi 6 (160 MHz, 25 dB):   {shannon(160e6, 25)/1e6:.2f} Mbps")
    print(f"Wi-Fi 6 welding (15 dB):    {shannon(160e6, 15)/1e6:.2f} Mbps")
    print(f"Nyquist (3100 Hz, 4 levels): {nyquist(3100, 4)/1e3:.1f} kbps")
    snr = 2 ** (56000 / 3100) - 1
    print(f"SNR for 56 kbps: {10*math.log10(snr):.1f} dB")