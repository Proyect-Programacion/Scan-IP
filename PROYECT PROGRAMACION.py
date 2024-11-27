from os import *

#PING
#arp -a

lista = list(popen("arp -a"))


print(lista[3])
#print(system("ping -a 192.168.56.255"))


