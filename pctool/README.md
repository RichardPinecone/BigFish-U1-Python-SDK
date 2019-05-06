# U1 EVB Boot Mode and Normal Mode
> U1 IOMOD pin is ON, and reset board, it will enter bootloader mode<br>
> U1 IOMOD pin is OFF, and reset board, it will enter normal mode<br>

![image](https://github.com/RichardPinecone/BigFish-U1-Python/blob/master/pctool/u1_evb.jpg)

# U1 Binary File Program
This window tool is developed based on .net framework<br>
It can be used to flash U1 CP, SP and AP <br>

    The U1 IOMOD pin shall be set to high and re-powerup to enter bootloader mode
    The U1 UART1 is used to flash U1, and it shall be configured as 921600,8,N,1 
    If the "UART1" textbox show "ccccc" which means the board in bootloader mode correctly

![image](https://github.com/RichardPinecone/BigFish-U1-Python/blob/master/pctool/u1_flash.jpg)

- "SP File" button is used to select the SP binary file
- "SP Download" button is used to download SP file
- "CP File" button is used to select the CP binary file
- "CP Download" button is used to download CP file
- "AP File" button is used to select the AP binary file
- "AP Download" button is used to download AP file

# Python REPL Console
Using Putty to connect EVB UART0 port and reset the EVB board, the log will be as following: <br>
CTRL+C is used to exit main.py and enter REPL mode <br>

![image](https://github.com/RichardPinecone/BigFish-U1-Python/blob/master/pctool/python_repl.jpg)
