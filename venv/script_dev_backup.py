from netmiko import ConnectHandler
from datetime import datetime
new123 = datetime.now()
myvariant_new123 = str(new123.day) + "-" + str(new123.month) + "-" + str(new123.year)
cred123=open(r"C:\Users\user\Music\crednotepad.txt","r")
new_cred123=cred123.read().splitlines()
user123=new_cred123[0]
pass123=new_cred123[1]
xyz=open(r"C:\Users\user\Music\multidevi.txt","r")
multidev123=xyz.read().splitlines()
for abc123 in multidev123:
    deviceinformation123={
        "username":user123,
        "password":pass123,
        "device_type":"cisco_ios",
        "ip":abc123,
    }
    ssh123=ConnectHandler(**deviceinformation123)
    print("taking the connection towards" + abc123)
    multicommand123=["show ip inter br","show run | in hostname","show clock","show ip protocol summary"
                     "show arp","show mac add","show log"]
    #for xyz123 in multicommand123:
       # print("#"*100)
        #print("this is output for " + xyz123)
       # print(ssh123.send_command(xyz123))
       # print("disconnected from " + abc123)
    cli123=ssh123.send_config_set(["logging host 3.3.3.3","router ospf 200","interface loopback 105","do sh ip inter br"])
    print(cli123)
    print("disconnect from " + abc123)
    #Taking backup
    newblankfile = open(r"C:\Users\user\Music\BACKUP\backup_" + abc123 + "-" + myvariant_new123 + ".txt", "a")
    saveoutput=newblankfile.write(cli123)
    newblankfile.close()
    #newblankfile = open(r"C:\Users\njexec\Music\BACKUP\backup_" + abc123 + "-" + myvariant_new123 + ".txt", "a")

    






