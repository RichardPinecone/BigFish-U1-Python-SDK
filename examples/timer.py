import pyb

# create TIMER instance, only support 0~3
a = pyb.TIMER(0)

# define one timer callback
def func(timer_channel)
   print("timer interrupt\n")

# set callback function
a.callback(func)

# set timer period to 500ms, unit is us, and timer is enabled automatically
a.period(500000)

# delay 10s
pyb.mdelay(10000)

# disable timer
a.disable()

