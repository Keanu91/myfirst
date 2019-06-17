import os
hostname = "192.168.0."
result = []
def ping(ip):
    response = os.system("ping -w 1 -n 1 " + ip)
    return(response,ip)

for i in range(0,254): #range of ip
    response = ping(hostname + str(i))
    val = response[1]
    if response[0] == 0:
        result.append(val)
print(result)
