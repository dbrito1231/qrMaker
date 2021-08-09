"""
@author: Damian Brito
@name: Windows Wifi QR
@date: 08/2021
@description: Used to pull connection details from currently connected WiFi
                and creates QR code. Only works for Windows devices only
                
Modules used:
    subprocess - used to run Windows commands
    Pandas - Used to clean data collected from subprocess
    wifi_qrcode_generator - used to create QR code with dataframe data
"""
import subprocess
import pandas as pd
import wifi_qrcode_generator

# sends netsh commands and splits current profile output into list
Id = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')

# eliminates unnecessary output before and after dataframe created
connectionData = [val.split(':') for val in Id[3:]]
toDelete = []

# loops through each list in connectionData to remove whitespace and newline characters
# andy newline chars or whitespace indexes are appended to toDelete.
for num in range(len(connectionData)):
    if len(connectionData[num]) > 1:
        # mac addresses are compacted back together since they are split by line 22
        if 'BSSID' not in connectionData[num][0] and 'Physical address' not in connectionData[num][0]:
            connectionData[num][0] = connectionData[num][0].strip()
            connectionData[num][1] = connectionData[num][1].rstrip('\r')
        else:
            connectionData[num][0] = connectionData[num][0].strip()
            mac = ':'.join(connectionData[num][1:]).strip('\r').strip()
            connectionData[num][1] = mac
            del connectionData[num][2:]
    else:
        toDelete.append(num)

# final cleaning for pulled data
connectionData = [val for val in connectionData if len(val) > 1]

# creating dataframe with clean data
# TODO: convert or migrate from df to series
formattedData = pd.DataFrame(connectionData).transpose()
newHeader = formattedData.iloc[0]
formattedData = formattedData[1:]
formattedData.columns = newHeader
        
# send netsh command to pull password and append to dataframe
password = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles',
        formattedData.Profile.item().strip(), 'key=clear']).decode('utf-8').split('\n')
formattedData['Password'] = str([b.split(":")[1][1:-1]
                    for b in password if "Key Content" in b])[2:-2]

# Prints out WiFi details
# TODO: output useful info from df
print("<~~~~ WiFi Details ~~~>")
print("    SSID:   ", formattedData.SSID.item().strip())
print("    Password:    ", formattedData.Password.item().strip())

# generate Qr code
qrImg = wifi_qrcode_generator.wifi_qrcode(formattedData.Profile.item().strip(), 
                                          False, 
                                          'WPA', 
                                          formattedData.Password.item().strip())
# outputs image to default picture viewer
qrImg.show()