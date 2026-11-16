import math

def utilisation(frame_bits, rate_bps, distance_m, window, speed=2e8):
    tx = frame_bits / rate_bps
    prop = distance_m / speed
    a = prop / tx
    u = window / (1 + 2 * a)
    return min(u, 1.0), a

if __name__ == "__main__":
    links = [("Campus LAN", 12000, 1e9, 192),
             ("City fibre", 12000, 1e9, 50e3),
             ("Satellite", 12000, 10e6, 36e6),
             ("Plant-HeadOffice", 12000, 1e9, 400e3)]
    for name, fb, rate, dist in links:
        u, a = utilisation(fb, rate, dist, 1)
        w = math.ceil(1 + 2 * a)
        print(f"{name:<17} a={a:8.2f}  stop-and-wait U={u*100:6.2f}%  window for 100%={w}")
    u, a = utilisation(12000, 10e6, 36e6, 64)
    print(f"Satellite SR W=64: U={u*100:.1f}%, throughput={u*10:.2f} Mbps")