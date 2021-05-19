import platform
import sys
import os
import ipaddress
import socket
for x in range(1):
    def node():
        print("Machine: ", end =" "), print(platform.machine())
        print("Hostname: ", end =" "), print(platform.node())
        print("CPU: ", end =" "), print(platform.processor())
        print("OS: ", end =" "), print(platform.platform())
        print("Version: ", end =" "), print(platform.version())
        print("IP_Address: ", end= " "),print(socket.gethostbyname('7313w001'))
    node()
    break
