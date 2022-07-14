import requests, argparse

parser = argparse.ArgumentParser(description='Get information about your IP or any other IP')

parser.add_argument('--ip', type=str, help='Enter IP to get information')

args = parser.parse_args()

def getdata(ip):
    if ip == None:
        ip = ""
    url = f"http://ip-api.com/json/{ip}?fields=66846719"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print("[ERROR] Unknown error")

def print_data():
    data = getdata(args.ip)
    if data["status"] == "success":
        isp = data["as"].split(" ")
        isp.pop(0)
        isp = " ".join(isp)
        if data["reverse"] == "":
            data["reverse"] = data["query"]
        print(f'IP: {data["query"]}\nCountry: {data["country"]}, {data["countryCode"]}\nRegion: {data["regionName"]}, {data["region"]}\nCity: {data["city"]}\nISP: {isp}\nReverse: {data["reverse"]}')
    else:
        print(f"[FAIL] {data['message']}")
print_data()