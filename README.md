# open-proxy-tester

![OPT](https://github.com/davift/open-proxy-tester/blob/main/image.png)

This tool aggregates multiple proxy lists, sorts them, and filters only the unique ones. Then, it tests if they effectively work and optionally even tests their throughput.

Related app https://github.com/rofl0r/proxychains-ng

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

## Dependencies

```
pip install -r requirements.txt
```
