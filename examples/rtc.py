import pyb

a=pyb.RTC()
a.datetime(2019,10,1,10,20,30,500)
a.datetime()

def testfunc():
  print("wakeup test\n")

a.wakeup(5,testfunc)
