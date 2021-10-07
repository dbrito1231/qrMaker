# WinWi QR
This project serves to generate a QR code with WiFi credentials for users to connect to the network.
The QR code is generated from a Windows command line (cmd or PS). The code is saved as a PNG file, 
where users can save the image locally or print.  This is useful for users who would like to connect to
someone's guest home WiFi.  The WiFi network that the computer is connected to will be available via the QR code.


### Prerequisites
* colorama: 0.4.4
* numpy: 1.21.2
* pandas: 1.3.3
* Pillow: 8.3.2
* python-dateutil: 2.8.2
* pytz: 2021.3
* qrcode: 7.3.1
* six: 1.16.0
* wifi-qrcode-generator: 0.1
* Windows based PC

### Files
* qrMaker.py: creates QR code

### Running the script & output
```
> qrMaker.py

<~~~~ WiFi Details ~~~>
    SSID:                 Name of WiFi network (ex. MyWiFi)
    Radio Type:           Type of radio being used (a/b/g/n/ac/ax) (ex. 802.11ac)
    Channnel:             Channel that WiFi is broadcasting on (ex. 120)
    Signal Strength:      Signal (ex. 83%)
    Security:             Type of security (ex. WPA/WPA3)

```

### Steps
1. Download or clone WinWi QR onto a Windows based computer.
2. Create virtualenv and install modules from requirements.txt.
3. Run script
4. The screen will output WiFi details, display the QR code, and save the image as
"wifi_qr.png".