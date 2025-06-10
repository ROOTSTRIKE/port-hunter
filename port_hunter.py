import argparse
import asyncio
import socket
from datetime import datetime

sem = None  # Global semaphore to control concurrency
output_file = None  # Optional output file

def banner():
    print(r"""
   ____             _     _             
  |  _ \ ___   ___ | |__ (_)_ __   __ _ 
  | |_) / _ \ / _ \| '_ \| | '_ \ / _` |
  |  __/ (_) | (_) | | | | | | | | (_| |
  |_|   \___/ \___/|_| |_|_|_| |_|\__, |
                                 |___/  
        🔥 Port Hunter by RootStrike
    """)

async def scan_port(ip, port, timeout):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        result = f"[+] {ip}:{port} is OPEN"
        print(result)
        if output_file:
            with open(output_file, "a") as f:
                f.write(result + "\n")
        writer.close()
        await writer.wait_closed()
    except:
        pass  # Port closed or filtered

async def scan_target(ip, ports, timeout, sleep):
    tasks = []
    for port in ports:
        await asyncio.sleep(sleep)
        async with sem:
            tasks.append(scan_port(ip, port, timeout))
    await asyncio.gather(*tasks)

def load_targets(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def parse_ports(port_str):
    if "-" in port_str:
        start, end = map(int, port_str.split("-"))
        return list(range(start, end + 1))
    return list(map(int, port_str.split(",")))

async def main():
    parser = argparse.ArgumentParser(description="Port Hunter - Async TCP Port Scanner by RootStrike")
    parser.add_argument("-iL", help="Input file with target IPs/domains", required=True)
    parser.add_argument("-p", help="Ports (e.g., 22,80,443 or 1-1000)", required=True)
    parser.add_argument("-t", type=float, help="Timeout per port in seconds", default=1.0)
    parser.add_argument("-s", type=float, help="Sleep between port attempts", default=0.1)
    parser.add_argument("-c", type=int, help="Max concurrent scans", default=100)
    parser.add_argument("-o", help="Output file to save results", default=None)
    args = parser.parse_args()

    global sem, output_file
    sem = asyncio.Semaphore(args.c)
    output_file = args.o

    targets = load_targets(args.iL)
    ports = parse_ports(args.p)

    banner()
    print(f"[INFO] Started scanning {len(targets)} target(s) across {len(ports)} ports...\n")

    start_time = datetime.now()
    jobs = [scan_target(ip, ports, args.t, args.s) for ip in targets]
    await asyncio.gather(*jobs)
    end_time = datetime.now()

    print(f"\n[FINISHED] Scan completed in {end_time - start_time}")
    if output_file:
        print(f"[SAVED] Results written to: {output_file}")

if __name__ == "__main__":
    asyncio.run(main())

