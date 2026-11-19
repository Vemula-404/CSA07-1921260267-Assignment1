# Task 7 – Error Detection

## CRC
Gen 1011, Data 1101011011.
Remainder = **001**.
Transmitted: **1101011011001**.

## 2-D Parity Blind Spot
4-corner flip (1,1), (1,4), (4,1), (4,4).
Every row/column has 2 flips = even parity. Not detected.

## Checksum
4500 + 0073 + 0000 + 4000 = 8573.
1's complement = **7A8C**.

## Parity vs CRC
Parity: catches odd errors, misses even.
CRC: catches bursts, misses multiples of polynomial.