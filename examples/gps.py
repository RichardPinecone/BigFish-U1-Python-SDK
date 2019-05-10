import pyb

a=pyb.GPS()
# start GPS and disable NB
a.start()

# delay 30sec for GPS check 
pyb.mdelay(30000)

# get GPS result 
print(a.result())

# stop GPS to enable NB again
a.stop() 
