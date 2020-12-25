import subprocess
import csv

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
#print(data)
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        with open('Wifi.csv', 'r+') as w:
            wifi_list = w.readlines()
            wifiList = []

            for line in wifi_list:
                entry = line.split(',')
                wifiList.append(entry[0])

            if wifi not in wifi_list:
                w.write(f'\n{wifi}, {results[0]}')

            else:
                w.append({wifi}, {results[0]})

        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Cannnot be Found')