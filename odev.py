import os
import ipaddress
from sys import argv
args = argv[-1]
targets = []
if "-" in args:
    start_ip = ipaddress.ip_address(args.split("-")[0])
    end_ip = ipaddress.ip_address(args.split("-")[-1])
    while start_ip <= end_ip:
        targets.append(str(start_ip))
        start_ip += 1
else:
    targets.append(args)
print("arama işlemi başlatılıyor..")
os.system("nmap -sn "+" ".join(targets)+" -oX output.xml") #burada xml dosyası oluşturuyoruz
print("arama işlemi bitti...")