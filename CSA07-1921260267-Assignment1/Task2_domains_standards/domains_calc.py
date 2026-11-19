def calculate_domains():
    hubs = 3
    coll_domains = hubs + 1 + 1  # 3 hubs + router link + phone switch
    bcast_domains = 2 # Router separates
    
    print(f"Collision domains: {coll_domains}")
    print(f"Broadcast domains: {bcast_domains}")
    
    # Alternative: Hubs replaced by switches
    coll_alt = hubs + 1 + 1 - 3 + 1  # Wait, one per hub port + uplinks
    # Actually: each switch = 1 per port. Simplified:
    print(f"With unmanaged switches: collision domains = 2 (uplinks only)")

if __name__ == "__main__":
    calculate_domains()