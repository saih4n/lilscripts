a = sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(psrc="192.168.2.1", pdst="192.168.2.1"),count=2)
