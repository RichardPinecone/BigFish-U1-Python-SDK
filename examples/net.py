import pyb

# create NET instance, and configure the server ip address to 192.168.0.1, port number to 8000, and TCP connect
a = pyb.NET(0, "192.168.0.1",8000,0)
# connect to server with 60s timeout
a.rconn(60000)
# send 123456 to server and timeout is 30s
a.rsend("123456", timeout=30000)
# receive 8 bytes from server and timeout is 20s
# if server reply data is bigger than 8, only 8bytes are gotten, others are ignored
# if server reply is litter than 8, the real received bytes are return
# if timeout occurs, return None
b = a.rrecv(8, timeout=20000)
if b == None:
  print("no recved from server\n")
else:
  print(b)

# using tcp to send 123456 to server 10.10.10.1, port 9000
# return the received data. 
# If timeout occurs, return None
# max return data bytes shall be less than 500bytes
ret = b.tcp_trans("10.10.10.1",9000,"123456",timeout=60000)
if ret == None:
  print("no recved from server\n")
else:
  print(ret)

# using udp to send 123456 to server 10.10.10.1, port 9000
# return the received data. 
# If timeout occurs, return None
# max return data bytes shall be less than 500bytes
ret = b.udp_trans("10.10.10.1",9000,"123456",timeout=60000)
if ret == None:
  print("no recved from server\n")
else:
  print(ret)

