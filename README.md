# BigFish-U1-Python
Based on MicroPython and add BigFish U1 support, and add the above feature for U1 product <br>

    Add GPS class for U1 feature
    Add NB class to get SIM card and module information
    Add NET class for easy network transfer
    Add PWM, I2C, SPI, RTC, PIN, UART class for U1 
    Add CTRL+X to enter and exit mode which can list and exec the special py file
    Add CTRL+L to enter py file flash mode
    Add class help() for function detail description

For more information: <br>
> MicoPython:  www.micropython.com  <br>
> BigFish:     www.fishsemi.com  <br>
# BigFish U1 Introduction
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

# Flash BIN files to U1
There are totally 3 binary files: cp.bin, ap.bin and sp.bin. <br>
The special PC tool can be used to program them <br>
[PC tool to Program U1](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/pctool) <br>

# Python Boot Sequence
- After powerup, the internal boot.py and main.py are executed automatically
- CTRL+C is used to exit the executing py file and enter REPL mode
- CTRL+L is used to enter the pyfile flash mode
- CTRL+X is used to enter and exit mode to execute the special py file.



