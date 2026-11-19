# Task 3 – Frame Analysis

## TTL Analysis
64 → 61 = 3 routers crossed.

## Overhead (12-byte payload)
14 + 20 + 20 + 12 + 4 = 70 bytes
Overhead = 58 bytes = **82.9%**

## Overhead (1400-byte payload)
1,458 bytes total -> **4.0%**

## Fault Mapping
MAC wrong -> Layer 2
TTL = 0 -> Layer 3 (ICMP Time Exceeded)
Port closed -> Layer 4 (TCP RST)