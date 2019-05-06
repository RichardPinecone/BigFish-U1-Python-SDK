import pyb

# create one NB instance
a = pyb.NB()

# check NB register state
# 0 - no register;  1 - registed, 2 - searching, 3 - denied, 4 - unknow, 5 - roaming
print(a.state())

# return imei
print(a.imei())

# return SIM card iccid
print(a.iccid())

# return cellinfo
print(a.cellinfo())

