#!/usr/bin/python3
import json

def export_foxyproxy_json():
    proxies = []
    proxies.append({
        "active": True,
        "title": "Tor",
        "type": "socks5",
        "hostname": "127.0.0.1",
        "port": "9050",
        "username": "",
        "password": "",
        "cc": "",
        "city": "",
        "color": "#9370db",
        "pac": "",
        "pacString": "",
        "proxyDNS": True,
        "include": [],
        "exclude": []
    })
    proxies.append({
        "active": True,
        "title": "Burp",
        "type": "http",
        "hostname": "127.0.0.1",
        "port": "8080",
        "username": "",
        "password": "",
        "cc": "",
        "city": "",
        "color": "#f5f5dc",
        "pac": "",
        "pacString": "",
        "proxyDNS": True,
        "include": [],
        "exclude": []
    })
    template = {
        "active": True,
        "title": "",
        "type": "socks5",
        "hostname": "",
        "port": "",
        "username": "",
        "password": "",
        "cc": "",
        "city": "",
        "color": "#bdb76b",
        "pac": "",
        "pacString": "",
        "proxyDNS": True,
        "include": [],
        "exclude": []
    }
    with open("socks5-speed.list", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                ip, port = line.split(":")
                proxy_entry = template.copy()
                proxy_entry["title"] = f"{ip}:{port}"
                proxy_entry["hostname"] = ip
                proxy_entry["port"] = port
                proxies.append(proxy_entry)
    foxyproxy_json = {
        "mode": "disable",
        "sync": False,
        "autoBackup": False,
        "passthrough": "",
        "theme": "",
        "container": {},
        "commands": {
            "setProxy": "",
            "setTabProxy": "",
            "quickAdd": ""
        },
        "data": proxies
    }
    with open("FoxyProxy.json", "w") as file:
        json.dump(foxyproxy_json, file, indent=2)

if __name__ == "__main__":
    export_foxyproxy_json()
