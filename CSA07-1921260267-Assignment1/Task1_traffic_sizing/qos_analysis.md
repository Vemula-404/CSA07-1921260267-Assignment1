# Task 1 – QoS Analysis

## Harm of 100 ms delay
1. Robot commands (CRITICAL) – misses 10 ms control loop
2. Vibration sensors (HIGH) – delayed alarms
3. Office ERP (MEDIUM) – visible sluggishness
4. CCTV (LOW) – buffered video

## FIFO problem
CCTV 1500-byte frames delay 200-byte robot commands by several ms.
10 ms deadline fails after just a few queued frames.
**QoS mandatory** (802.1p priority).