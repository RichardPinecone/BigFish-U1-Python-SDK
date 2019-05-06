# 1. BigFish-U1-Python
Based on MicroPython and add BigFish U1 support, and add the following features for U1 product <br>

    - GPS class for U1 feature
    - NB class to get SIM card and module information
    - NET class for easy network transfer
    - PWM, I2C, SPI, RTC, PIN, UART class for U1 
    - CTRL+X to enter and exit mode which can list and exec the special py file
    - CTRL+L to enter py file flash mode
    - Class help() for function detail description

For more information: <br>
> MicoPython:  www.micropython.com  <br>
> BigFish:     www.fishsemi.com  <br>
# 2. BigFish U1 Introduction
BigFish U1 is one NB-IOT SOC, and it contains three Cortex-M4: CP, SP, and AP<br>
> CP is used for Modem and NB protocol<br>
> SP is for security and Network(TCP/IP) protocols<br>
> AP is used for application and currently micropython is running on it.<br>

The hardware Mailbox and Share RAM are used to commnunication between CP/AP and SP/AP.<br>

U1 Supports:<br>
- 2M internal flash and 1M RAM.  
- 4 x PWM
- 2 x SPI
- 4 x UART
- 2 x I2C
- 4 x Timer
- 1 x RTC
- 40 x GPIO

# 3. Setup Environment based on U1 EVB
## 3.1 Flash binary files
- There are totally 3 binary files: cp.bin, ap.bin and sp.bin. <br>
- The special PC tool can be used to program them <br>
[PC tool to Program U1](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/pctool) <br>
## 3.2 Python Console
For U1 EVB, UART0/1 has been connected to one UART<->USB chip, and there will be two COM ports in PC<br>
- UART1 is used to binary flash, and shall be 921600, 8, 1, N
- The UART0 of U1 is used as Python Console port, and shall be 9600, 8, 1, N<br>

# 4. Python Boot Sequence
- After powerup, the internal boot.py and main.py are executed automatically
- CTRL+C is used to exit the executing py file and enter REPL mode
- CTRL+L is used to enter the pyfile flash mode
- CTRL+X is used to enter and exit mode to execute the special py file.

# 5. NB运营商限制
- 电信COAP连接电信服务器
- 电信TCP可以连接自建服务器
- 电信UDP不能连接自建服务器
- 移动TCP可以连接自建服务器
- 移动UDP可以连接自建服务器

# 6. NB网络服务器例子
[Server For U1 Network Test](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/server) <br>

