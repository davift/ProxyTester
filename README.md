# ProxyTester

![OPT](https://github.com/davift/ProxyTester/blob/main/image.png)

This tool aggregates multiple proxy lists, sorts them, and filters only the unique ones. Then, it tests if they effectively work and optionally even tests their throughput.

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

Proxy servers are grouped as follows.

- socks5-source.list
  - A list or URLs that contains lists of proxy servers from multiple sources.
- socks5-unique.list
  - .
- socks5-latency.list
  - .
- socks5-speed.list
  - .

## FoxyProxy Export Usage

Import from URL:

https://github.com/davift/ProxyTester/raw/refs/heads/main/FoxyProxy.json

## Dependencies

```
pip install -r requirements.txt
```
