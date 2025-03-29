#!/usr/bin/python3
import requests
import concurrent.futures
import re
import time
import argparse

def fetch_lists():
  print("[ Fetching Proxy Lists ]")
  with open('socks5-source.list', 'r') as file:
    lists = file.readlines()
  servers = []
  for list in lists:
    list = list.strip()
    try:
      response = requests.get(list)
      print('■', end='', flush=True)
      for line in response.text.splitlines():
        match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)', line)
        if match:
          servers.append(match.group(1))
    except requests.RequestException as e:
      print('☐', end='', flush=True)
  with open('socks5-unique.list', 'w') as output_file:
    servers = sorted(set(servers))
    for server in servers:
      if not (server.startswith("0.0.0.0") or server.startswith("10.") or server.startswith("172.16.") or server.startswith("172.31.") or server.startswith("192.168.")):
        output_file.write(server + '\n')
  print("")

def proxy_test(proxy):
  try:
    response = requests.get("https://1.1.1.1/cdn-cgi/trace.json", proxies={"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}, timeout=5)
    if "python-requests" in response.text:
      if response.status_code == 200:
        duration = response.elapsed.total_seconds()
        print('■', end='', flush=True)
        #print(f"{proxy} - {duration} seconds")
        return proxy, duration
  except requests.RequestException as e:
    pass
  print('☐', end='', flush=True)
  return

def proxy_test_servers():
  print("[ Testing Proxy ]")
  with open("socks5-unique.list", "r") as file:
    proxies = [line.strip() for line in file if line.strip()]
  with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = list(executor.map(proxy_test, proxies))
  working_proxies = [result for result in results if result is not None]
  working_proxies.sort(key=lambda x: x[1])
  i = 0
  print("\n  [ Lowest Latency ]")
  with open("socks5-latency.list", "w") as output_file:
    for proxy, duration in working_proxies:
      if i < 10:
        i += 1
        print(f"  {proxy} ({duration:.3f}s)")
      output_file.write(f"{proxy}\n")

def speed_test(proxy):
  url = "https://link.testfile.org/15MB"
  output_path = "/dev/shm/a8f5466bdf7b2411e4a0e403850a1918"
  response = requests.get(url, proxies={"http": f"socks5://{proxy}", "https": f"socks5://{proxy}"}, stream=True, timeout=5)
  response.raise_for_status()
  with open(output_path, 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
      file.write(chunk)

def speed_test_servers():
  print("[ Testing Speed ]")
  with open('socks5-latency.list', 'r') as file:
    proxies = file.readlines()
  proxies = proxies[:50]
  tested = []
  for proxy in proxies:
    proxy = proxy.strip()
    if proxy:
      start_time = time.time()
      try:
        speed_test(proxy)
        end_time = time.time()
        duration = end_time - start_time
        print('■', end='', flush=True)
        tested.append((proxy, duration))
      except Exception as e:
        print('☐', end='', flush=True)
  tested.sort(key=lambda x: x[1])
  print("\n  [ Download Duration ]")
  with open("socks5-speed.list", "w") as output_file:
    for proxy, duration in tested:
      print(f"  {proxy} ({duration:.3f}s)")
      output_file.write(f"{proxy}\n")

def main():
  parser = argparse.ArgumentParser(description="Open Proxy Tester")
  parser.add_argument('--fetch', action='store_true', help='Fetch proxy lists')
  parser.add_argument('--test', action='store_true', help='Test proxy servers')
  parser.add_argument('--speed', action='store_true', help='Speed test using proxies')
  parser.add_argument('--all', action='store_true', help='All steps: fetch, test, speed')
  args = parser.parse_args()

  if args.fetch:
    fetch_lists()
    exit()
  if args.test:
    proxy_test_servers()
    exit()
  if args.speed:
    speed_test_servers()
    exit()
  if args.all:
    fetch_lists()
    proxy_test_servers()
    speed_test_servers()
    exit()
  else:
    if input("Fetch proxy lists? (y/n): ").strip().lower() == 'y':
      fetch_lists()
    if input("Test all servers? (y/n): ").strip().lower() == 'y':
      proxy_test_servers()
    if input("Perform speed test? (y/n): ").strip().lower() == 'y':
      speed_test_servers()
    exit()

if __name__ == "__main__":
  main()

