def analyze_frame(ttl_start=64, ttl_end=61, payload_bytes=12):
    routers = ttl_start - ttl_end
    print(f"Routers crossed: {routers}")
    
    # Size calc
    eth_hdr = 14
    ip_hdr = 20
    tcp_hdr = 20
    fcs = 4
    total = eth_hdr + ip_hdr + tcp_hdr + payload_bytes + fcs
    print(f"Payload: {payload_bytes}B, Total: {total}B")
    print(f"Overhead: {(total - payload_bytes)/total*100:.1f}%")

if __name__ == "__main__":
    analyze_frame()