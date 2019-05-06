# U1 Python Introduction
After Powerup, the boot.py and main.py will be executed if they exist.<br>
The CTRL+C can be used to interrrupt the pyfile executing and enter REPL mode. <br>
# U1 Python Functions
module "pyb" is used to implement all hardware relevant features <br>
- micros():     return microseconds after power up<br>
    > import pyb<br>
    > print(pyb.micros())<br>
- millis():     return milliseconds after power up<br>
    > import pyb<br>
    > print(pyb.millis())<br>
- mdelay(n):     delay milliseconds<br>
    > import pyb<br>
    > \# delay 1sec<br>
    > pyb.mdelay(1000) <br>
- udelay(n):     delay microseconds<br>
    > import pyb<br>
    > \# delay 1sec<br>
    > pyb.udelay(1000000) <br>
- disable_interrupt():     disable hardware interrupt<br>
    > import pyb<br>
    > pyb.disable_interrupt()<br>
- enable_interrupt():     enable hardware interrupt<br>
    > import pyb<br>
    > pyb.enable_interrupt()<br>
- wfi():     enter ARM WFI mode<br>
    > import pyb<br>
    > pyb.wfi()<br>
- mem_read(m):     read memory<br>
    > import pyb<br>
    > \# read address 0xb0030000<br>
    > print(pyb.mem_read(0xb0030000))  <br>
- mem_write(m, v):     write memory<br>
    > import pyb<br>
    > \# write 0x11223344 to address 0xb0030000<br>
    > pyb.mem_read(0xb0030000, 0x11223344)  <br>
- flash_erase(a,s):     erase flash from address "a" to "a + s - 1"<br>
    > import pyb<br>
    > \# erase 2K flash from address 0x30000<br>
    > pyb.flash_erase(0x30000, 2048)  <br>
- flash_program(a,b):     program data "b" to flash address "a"<br>
    > import pyb<br>
    > \# write "12345" to flash from address 0x30000 <br>
    > pyb.flash_erase(0x30000, "12345")  <br>
# U1 Python RTC Class<br>
- class RTC():     system RTC<br>
    > import pyb<br>
    > a=pyb.RTC()<br>
    > \# set current RTC to 2019/10/1 8:9:20.100 <br>
    > a.datetime(2019,10,1,8,9,20,100) <br>
    > \# return currently RTC value<br>
    > a.datetime()  <br>
    > \# delay 5 second to call function to output "wakeup test" <br>
    > def func():<br>
    > ... print("wakeup test\n") <br>
    > a.wakeup(5,func) <br>
# U1 Python GPS Class<br>
- class GPS():     system GPS position access
    > import pyb<br>
    > a=pyb.GPS()<br>
    > \# start GPS <br>
    > a.start()<br>
    > \# delay 30sec for GPS check <br>
    > pyb.mdelay(30000)<br>
    > \# get GPS result <br>
    > a.value()  <br>
    > a.stop() <br>
- class NB() <br>   system NB modem relevant information
- class NET() <br>   system NET network transfer 
- class PWM() <br>   system PWM 
- class TIMER() <br>   system TIMER
- class SPI() <br>   system SPI
- class I2C() <br>   system I2C
- class UART() <br>   system UART
- class PIN() <br>   system PIN
