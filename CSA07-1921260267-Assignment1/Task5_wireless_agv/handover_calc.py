def handover(distance, spacing, time_ms):
    handovers = distance / spacing
    total_ms = handovers * time_ms
    print(f"Distance {distance}m / Spacing {spacing}m = {handovers:.0f} handovers")
    print(f"Unreachable time: {total_ms:.0f} ms")

if __name__ == "__main__":
    print("--- Wi-Fi ---")
    handover(1200, 30, 150)
    print("--- 5G ---")
    handover(1200, 300, 20)