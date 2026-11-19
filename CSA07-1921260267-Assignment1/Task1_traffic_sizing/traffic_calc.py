def line_traffic():
    robots = 40 * (200 * 8) / 0.002
    sensors = 600 * 50 * 8
    cctv = 24 * 4_000_000
    office = int(150 * 0.10) * 2_000_000
    total = robots + sensors + cctv + office
    
    print(f"Robots:  {robots/1e6:7.2f} Mbps")
    print(f"Sensors: {sensors/1e6:7.2f} Mbps")
    print(f"CCTV:    {cctv/1e6:7.2f} Mbps")
    print(f"Office:  {office/1e6:7.2f} Mbps")
    print(f"Total per line: {total/1e6:.2f} Mbps")
    print(f"Plant (8 lines): {total*8/1e6:.2f} Mbps")

    # Motion-triggered alternative
    cctv_alt = cctv * 0.05
    total_alt = robots + sensors + cctv_alt + office
    print(f"\nIf CCTV motion-triggered (5%): {total_alt/1e6:.2f} Mbps/line")
    print(f"Plant: {total_alt*8/1e6:.2f} Mbps")

if __name__ == "__main__":
    line_traffic()