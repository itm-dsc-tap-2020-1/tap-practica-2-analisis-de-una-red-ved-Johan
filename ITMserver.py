import os

hostname="www.itmorelia.edu.mx"

respuesta=os.system("ping -c 1 "+hostname)

if respuesta==0:
    print(hostname + ": esta en funcionamiento")
else:
    print(hostname + ": no funciona")

comp="200.33.171.0/24"

os.system("nmap -sP "+comp)

'''
PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=61 time=24.6 ms

--- denebvirtual.itmorelia.edu.mx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 24.606/24.606/24.606/0.000 ms
www.itmorelia.edu.mx: esta en funcionamiento

Starting Nmap 7.60 ( https://nmap.org ) at 2020-02-27 11:40 CST
Stats: 0:00:20 elapsed; 0 hosts completed (0 up), 256 undergoing Ping Scan
Ping Scan Timing: About 42.29% done; ETC: 11:41 (0:00:27 remaining)
Stats: 0:00:21 elapsed; 0 hosts completed (0 up), 256 undergoing Ping Scan
Ping Scan Timing: About 43.16% done; ETC: 11:41 (0:00:28 remaining)
Stats: 0:00:52 elapsed; 0 hosts completed (0 up), 256 undergoing Ping Scan
Ping Scan Timing: About 88.77% done; ETC: 11:41 (0:00:07 remaining)
Stats: 0:00:52 elapsed; 0 hosts completed (0 up), 256 undergoing Ping Scan
Ping Scan Timing: About 92.29% done; ETC: 11:41 (0:00:04 remaining)
Stats: 0:00:53 elapsed; 0 hosts completed (0 up), 256 undergoing Ping Scan
Ping Scan Timing: About 97.27% done; ETC: 11:41 (0:00:01 remaining)
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.0090s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.019s latency).
Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
Host is up (0.0071s latency).
Nmap scan report for 200.33.171.66
Host is up (0.023s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.0064s latency).
Nmap scan report for 200.33.171.86
Host is up (0.0083s latency).
Nmap scan report for 200.33.171.99
Host is up (0.013s latency).
Nmap done: 256 IP addresses (7 hosts up) scanned in 53.89 seconds
'''