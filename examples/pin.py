import pyb

# create instance for GPIO0
a=pyb.PIN(0)

# set GPIO to output mode
a.mode(a.OUT)

# set GPIO0 output high
a.value(1)

# set GPIO0 output low
a.value(1)

# create instancee for GPIO1 with input mode
b=pyb.PIN(1,pyb.PIN.IN)

# get GPIO1 state
print(b.value())

# GPIO rising interrupt callback
def func(pin):
  print("gpio interrupt\n")
  
# set GPIO1 interrupt callback function
b.callback(func)

# rising edge trigger interrupt
b.int_mode(b.IT_RISING)

# enable interrupt
b.int_enable()
