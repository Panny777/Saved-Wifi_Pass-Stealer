import subprocess
import csv

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for wifi in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        with open('Wifi.csv', 'r+') as w:
            wifi_list = w.readlines()
            wifiList = []

            for line in wifi_list:
                entry = line.split(',')
                wifiList.append(entry[0])
            try:
                w.write(f'\n {wifi}, {results[0]}')
                print ("{:<30}|  {:<}".format(wifi, results[0]))                
                    
            except IndexError:
                no_pass = ""
                w.write(f'\n{wifi}, {no_pass}')
                print ("{:<30}|  {:<}".format(wifi, ""))
    except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")
exit()
