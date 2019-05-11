# BigFish U1 Introduction
BigFish U1 is one NB-IOT SOC, and it contains three Cortex-M4: CP, SP, and AP<br>

| Cortex-M4 | Function | Resource |
|----|:----:|:-----:|
|  CP | Modem and NB protocol |  |
|  SP | Security and Network(TCP/IP) protocol  |  |
|  AP | Application (micropython) |  |

The hardware Mailbox and Share RAM are used to data transfer between CP/AP and SP/AP.<br>

U1 Supports:<br>
- 2M internal flash and 1M RAM.  
- 4 x PWM
- 2 x SPI
- 4 x UART
- 2 x I2C
- 4 x Timer
- 1 x RTC
- 40 x GPIO

# BigFish U1 Python SDK
## 为何使用Python环境
- Python易学易用，当前最热门的语言 <br>
- 无需搭建编译环境<br>
- 快速功能验证和开发，适合行业细分的IOT市场<br>
- 接口简单，稳定，代码量 < 1% 的C语言<br>
- 远程升级调试方便<br>

## BigFish U1 Python功能描述
Based on MicroPython and Add BigFish U1 support<br>
The following features are implemented to support BigFish U1 <br>

    - GPS class for U1 feature
    - NB class to get SIM card and module information
    - NET class for easy network transfer
    - PWM, I2C, SPI, RTC, PIN, UART class for U1 
    - CTRL+X to enter and exit mode which can list and exec the special py file
    - CTRL+L to enter py file flash mode
    - Class help() for function detail description
    - Mailbox data transfer between AP and SP
    - Mailbox data transfer between AP and CP

For more information: <br>
> MicoPython:  www.micropython.com  <br>
> BigFish:     www.fishsemi.com  <br>

# BigFish U1 EVB上搭建python环境
For U1 EVB, UART0/1 has been connected to one UART<->USB chip, and there will be two COM ports in PC<br>
- UART1 is used to binary flash, and shall be 921600, 8, 1, N
- UART0 of U1 is used as Python Console port, and shall be 9600, 8, 1, N<br>

## Flash Binary Files
Download 3 binary files: cp.bin, ap.bin and sp.bin, and flash them to EVB board. <br>
### Window工具
Using [BigFishU1Program.exe](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/pctool)  to Program U1<br>
### Linux工具
TODO ...

# Python Console
User can use python console to control and test all features of EVB board
It also be used to program the final py file for product release.
## Window工具
Using [PuTTY_0.67.0.0.exe](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/pctool) to connect EVB UART0 with 9600,8,1,N.

## Linux工具
Using minicom

## Board Power Up
After power reset, there is python log information in UART0:

    Executing boot.py
    Exit boot.py
    Executing main.py
    Boot Function ...
    CTRL+C exit main.py

The CTRL+C can be used to interrrupt it and enter REPL mode.<br>
- In REPL mode, you can verify all features refer to [the examples](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/examples)  <br>
- In REPL mode, help() can be used to list all support modules. <br>
- For more micropython usage, please refer to www.micropython.org <br>
## Python REPL
What is REPL? REPL is the language shell. Its short for Read, Eval, Print and Loop.<br>
The process is:<br>
> Read: take user input. <br>
> Eval: evaluate the input.<br>
> Print: shows the output to the user.<br>
> Loop: repeat.<br>
## Flash Python file for auto-run

    There is some issue in internal flash, so this feature can not test currently<br>
    
## Python Boot Sequence and Special input key
- After powerup, the internal boot.py and main.py are executed automatically
- CTRL+C is used to exit the executing py file and enter REPL mode
- CTRL+L is used to enter the pyfile flash mode
- CTRL+X is used to enter and exit mode to execute the special py file.

# 当前限制
- 目前U1内部Flash更新有问题，所有暂时不能升级内部自动运行的pyfile. <br>
- 目前仅仅支持REPL模式测试功能 <br>
- 针对每个模块的callback函数，有一些使用限制，详细参考相关模块<br>

# NB运营商限制
- 电信COAP连接电信服务器
- 电信TCP可以连接自建服务器
- 电信UDP不能连接自建服务器
- 移动TCP可以连接自建服务器
- 移动UDP可以连接自建服务器

# NB网络服务器例子
[Server For U1 Network Test](https://github.com/RichardPinecone/BigFish-U1-Python/tree/master/server) <br>

