import argparse
import asyncio
import socket

sem = None  # Global semaphore (used to control concurrency)

async def scan_port(ip, port, timeout):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        print(f"[+] {ip}:{port} is OPEN")
        writer.close()
        await writer.wait_closed()
    except:
        pass  # Silence closed ports

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
    parser = argparse.ArgumentParser(description="Port Hunter by RootStrike")
    parser.add_argument("-iL", help="Input file with list of IPs/domains", required=True)
    parser.add_argument("-p", help="Ports (e.g., 22,80,443 or 1-1000)", required=True)
    parser.add_argument("-t", type=float, help="Timeout per port (seconds)", default=1.0)
    parser.add_argument("-s", type=float, help="Sleep between port attempts (seconds)", default=0.1)
    parser.add_argument("-c", type=int, help="Max concurrent scans", default=100)
    args = parser.parse_args()

    global sem
    sem = asyncio.Semaphore(args.c)

    targets = load_targets(args.iL)
    ports = parse_ports(args.p)

    print(f"[INFO] Scanning {len(targets)} hosts on {len(ports)} ports each...")

    jobs = [scan_target(ip, ports, args.t, args.s) for ip in targets]
    await asyncio.gather(*jobs)

if __name__ == "__main__":
    asyncio.run(main())
