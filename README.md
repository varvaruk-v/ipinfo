# ShowIP

ShowIP is a Python tool that shows your IP and the DNS server you use.
You can also view information about any IP address or domain.

## Executable ([Windows™](https://en.wikipedia.org/wiki/Microsoft_Windows) only)
1. Download "myip.exe" file from releases
2. Open it in the CMD

## Installation (any OS)

Use the package manager [pip](https://pypi.org/project/showip/) to install ShowIP.

```bash
pip install showip
```

## Usage
### 1) Displays information about your IP address and the DNS server you use
#### Type in console
```bash
showip
```
**or**
```bash
myip
```
Output:
```bash
IP: 8.8.8.8
Country: United States, US
Region: Virginia, VA
City: Ashburn
ISP: Google LLC
Reverse: dns.google
----------------------------
DNS: 8.8.8.8(United States - Google LLC)
```
### 2) Use parameter "-ip" to see information about any IP addresses or domain
#### Type in console
```bash
showip -ip [DOMAIN OR IP ADDRESS]
```
**or**
```bash
myip -ip [DOMAIN OR IP ADDRESS]
```
Output:
```bash
IP: 142.251.39.110
Country: Netherlands, NL
Region: North Holland, NH
City: Amsterdam
ISP: Google LLC
Reverse: ams15s48-in-f14.1e100.net
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
