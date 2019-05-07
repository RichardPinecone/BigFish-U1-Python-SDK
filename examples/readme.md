# U1 Python Introduction
- After Powerup, the boot.py and main.py will be executed if they exist.<br>
- The CTRL+C can be used to interrrupt the pyfile executing and enter REPL mode. <br>
- For basic python modules, please refer to www.micropython.org <br>

# U1 Python Functions
module "pyb" is used to implement all hardware relevant features <br>
- micros():     return microseconds after power up<br>

        import pyb
        print(pyb.micros())
    
- millis():     return milliseconds after power up<br>

        import pyb
        print(pyb.millis())
        
- mdelay(n):     delay milliseconds<br>

        import pyb
        # delay 1sec
        pyb.mdelay(1000) 
        
- udelay(n):     delay microseconds<br>

        import pyb
        # delay 1sec
        pyb.udelay(1000000)
        
- disable_interrupt():     disable hardware interrupt<br>

        import pyb
        pyb.disable_interrupt()
        
- enable_interrupt():     enable hardware interrupt<br>

        import pyb
        pyb.enable_interrupt()
        
- wfi():     enter ARM WFI mode<br>

        import pyb
        pyb.wfi()
        
- mem_read(m):     read memory<br>

        import pyb
        # read address 0xb0030000
        print(pyb.mem_read(0xb0030000))
        
- mem_write(m, v):     write memory<br>

        import pyb
        # write 0x11223344 to address 0xb0030000
        pyb.mem_read(0xb0030000, 0x11223344)
        
- flash_erase(a,s):     erase flash from address "a" to "a + s - 1"<br>

        import pyb
        # erase 2K flash from address 0x30000
        pyb.flash_erase(0x30000, 2048)
        
- flash_program(a,b):     program data "b" to flash address "a"<br>

        import pyb
        # write "12345" to flash from address 0x30000
        pyb.flash_erase(0x30000, "12345")
        
# U1 Python RTC Class<br>
class RTC():     system RTC<br>
## Constructor:
> class pyb.RTC()<br>

Construct and return RTC object
## General Methods
> RTC.datetime(\[{year, month, day, hour, minute, second, millsecond}\])<br>

Set and Get real time clock<br>
If no augments, return 7-tuple with the current date and time<br>

> RTC.wakeup(delay_ms, callback)<br>

Set RTC wakeup delay, and after "delay_ms", the callback function will be called<br>
The callback function shall be no augment<br>

> RTC.help()<br>

It will describe all RTC functions in detail<br>

## Examples
[rtc example: rtc.py](./rtc.py) <br>

# U1 Python GPS Class<br>
class GPS():     system GPS position access<br>
## Constructor:
> class pyb.GPS()<br>

Construct and return GPS object
## General Methods
> GPS.start()<br>

Enable GPS feature. The NB is disabled automatically when GPS is enabled<br>

> GPS.stop()<br>

Disable GPS feature. The NB is re-enabled automatically when GPS is disabled<br>

> GPS.result()<br>

Get GPS result, return 3-tuple with GPS time, Latitude, Longitude<br>
If there is not available GPS data, it will return None<br>

> GPS.help()<br>

It will describe all GPS functions in detail<br>

## Examples
[gps example: gps.py](./gps.py) <br>
# U1 Python NB Class<br>
class NB():     system NB modem relevant information<br>
## Constructor:
> class pyb.NB()<br>

Construct and return NB object
## General Methods
> NB.imei()<br>

Get IMEI of NB module, the return is bytes type<br>
> NB.iccid()<br>

Get ICCID of SIM card, the return is bytes type<br>
> NB.help()<br>

It will describe all NB functions in detail<br>

## Examples
[nb example: nb.py](./nb.py) <br>
# U1 Python NET Class<br>
class NET():     system NET network transfer <br>
Currently, five network connection channels are supported 
## Constructor:
> class pyb.NET(n\[,ipaddress,portnum,udp_mode\])<br>

Usinged network connection channel index to construct and return the relevant NET object. <br>
- n shall be 0~4.
- ipaddrss is the IP address of remote server
- port num is the connnect port number of remote server
- udp_mode:  0 means TCP connect mode, 1 means UDP connection mode
## General Methods
> NET.remote(\[ipaddress,portnum,udp_mode\])<br>

The augments are same as construct.
> NET.rconn()<br>

Connect the remote server according the construct or remote configure server ip, port and connect mode<br>
> NET.rsend(data, timeout=n)<br>

Send bytes/string "data" to server. The timeout unit is ms<br>
> NET.rrecv(num, timeout=n)<br>

Received the "num" bytes from server. The timeout unit is ms<br>
- If timeout occurs, return None.<br>
- If the server send data is more than "num" bytes, only "num" bytes are returned, others are discarded<br>
- If the server send data is less than "num" bytes, all data are returned<br>

> NET.rclose()<br>

Close the connection with the relevant remote server

> NET.tcp_trans(ipaddr, port, data, timeout=n)<br>

Using TCP to transfer data with the special server which ip and port are defined in auguments<br>

> NET.udp_trans(ipaddr, port, data, timeout=n)<br>

Using UDP to transfer data with the special server which ip and port are defined in auguments<br>

## Examples
[net example: net.py](./net.py) <br>
# U1 Python PWM Class<br>
- class PWM():     system PWM <br>
    [pwm example: pwm.py](./pwm.py) <br>
# U1 Python TIMER Class<br>
- class TIMER():     system TIMER<br>
    [timer example: timer.py](./timer.py) <br>
# U1 Python SPI Class<br>
- class SPI():     system SPI<br>
    [spi example: spi.py](./spi.py) <br>
# U1 Python I2C Class<br>
- class I2C():    system I2C<br>
    [spi example: i2c.py](./i2c.py) <br>
# U1 Python UART Class<br>
- class UART():     system UART<br>
    [uart example: uart.py](./uart.py) <br>
# U1 Python UART Class<br>
- class PIN():     system PIN<br>
    [pin example: pin.py](./pin.py) <br>
