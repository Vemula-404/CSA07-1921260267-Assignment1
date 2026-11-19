# Task 6 – Ethernet Diagnostics

## Late Collision + CRC Error
Causes: **Duplex mismatch** (forced half on one end, auto/full on other).
Fix: set both ends to auto/auto, or force 100/full on both.

## MAC 01:00:5e:0a:01:02
First byte 0x01 = multicast (LSB=1).
Belongs to IPv4 multicast group range.

## Jumbo Frames
9000 bytes. Cuts overhead.
**Risk:** All devices must support. One 1500B device = silent drop.
Use ONLY in dedicated storage VLAN, never on robot shop floor.