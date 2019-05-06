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
- class RTC():     system RTC<br>
    [rtc example: rtc.py](./rtc.py) <br>
# U1 Python GPS Class<br>
- class GPS():     system GPS position access<br>
    [gps example: gps.py](./gps.py) <br>
# U1 Python NB Class<br>
- class NB():     system NB modem relevant information<br>
    [nb example: nb.py](./nb.py) <br>
# U1 Python NET Class<br>
- class NET():     system NET network transfer <br>
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
