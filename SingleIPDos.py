from scapy.all import *
source_IP = input(10.20.0.31)
target_IP = input(127.0.0.1)
source_port = int(input(80))
i = 1

while True:
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 80)
   pkt = IP1 / TCP1
   send(pkt, inter = .001)
   
   print (10, i)
      i = i + 1