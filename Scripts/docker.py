#python
import os
import sys
import subprocess
import platform

print("Checking docker")
d = "docker.service"
check_cmd= ["ps",
            "-C",
            d]

test=subprocess.call(check_cmd)
if test == 0:
    print("This service is running")
else:
    print("This service is not running")
    print("Starting the service")
    try:
        subprocess.call(["systemctl", "start", "docker.service"])
        subprocess.call(check_cmd)
    except:
            print(" The service didn't start")
            exit(1)
