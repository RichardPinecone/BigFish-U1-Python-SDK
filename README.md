# BigFish-U1-Python
Based on micropython and add bigfish U1 support

# BigFish U1 Introduction
BigFish U1 is one NB-IOT SOC, and it contains three Cortex-M4: CP, SP, and AP
CP is used for Modem and NB protocol
SP is for security and Network(TCP/IP) protocols
AP is used for application and currently micropython is running on it.
The hardware Mailbox and Share RAM are used to commnunication between CP/AP and SP/AP.

U1 supports:
- 2M internal flash and 1M RAM.  
- 4 x PWM
- 2 x SPI
- 4 x UART
- 2 x I2C
- 4 x Timer
- 1 x RTC
- 40 x GPIO

# Flash BIN files to U1
There are totally 3 binary files: cp.bin, ap.bin and sp.bin. <br>
The special PC tool can be used to program them <br>
[PC tool to Program U1](./pctool/readme.md) <br>




