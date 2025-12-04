import winrm

s = winrm.Session('http://192.168.1.105:5985/wsman', auth=('ansible','BoatyBoatman123'))
print(s.run_cmd('hostname').std_out)
