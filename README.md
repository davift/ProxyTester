# ProxyTester

![OPT](https://github.com/davift/ProxyTester/blob/main/image.png)

This tool aggregates multiple proxy lists, sorts them, and filters only the unique ones. Then, it tests if they effectively work and optionally even tests their throughput.

- socks5-source.list
  – URLs of proxy sources.
- socks5-unique.list
  – Unique, sorted proxy servers.
- socks5-latency.list
  – Servers sorted by lowest latency.
- socks5-speed.list
  – Top 50 servers that downloaded a 15 MB file.

Related apps:

- ProxyChains - https://github.com/rofl0r/proxychains-ng
- FoxyProxy - https://github.com/foxyproxy/browser-extension

## Usage

```
usage: socks5.py [-h] [--fetch] [--test] [--speed] [--all]

Open Proxy Tester

options:
  -h, --help  show this help message and exit
  --fetch     Fetch proxy lists
  --test      Test proxy servers
  --speed     Speed test using proxies
  --all       All steps: fetch, test, speed
```

## ProxyChains Usage

The following commands will create a new configuration file from the existing one replacing the list of servers.

```
sed -n '/^[^#]/p' /etc/proxychains4.conf | sed '/\[ProxyList\]/q' | tee ~/proxychains-socks5-list.conf
curl -s -f https://raw.githubusercontent.com/davift/ProxyTester/refs/heads/main/socks5-speed.list | sed -E 's/^([^:]+):([^:]+)$/socks5 \1 \2/' | tee -a ~/proxychains-socks5-list.conf
proxychains -f ~/proxychains-socks5-list.conf curl ip.me
```

## FoxyProxy Export Usage

Import from URL:

https://github.com/davift/ProxyTester/raw/refs/heads/main/FoxyProxy.json

## Dependencies

```
pip install -r requirements.txt
```
