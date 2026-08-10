#!/usr/bin/env python3

"""
Simple TCP Port Scanner

Description: A simple TCP port scanner written in Python for learning purposes and authorized security testing.
"""

import argparse
import time
from scanner import scan_ports
from output import print_results


def main():

    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")

    parser.add_argument("target", help="Target IP address or hostname")

    parser.add_argument(
        "-s", "--start", type=int, default=1, help="Start port (default: 1)"
    )

    parser.add_argument(
        "-e", "--end", type=int, default=1024, help="End port (default: 1024)"
    )

    parser.add_argument(
        "-t", "--threads", type=int, default=50, help="Number of threads"
    )

    parser.add_argument("--timeout", type=float, default=1, help="Connection timeout")

    args = parser.parse_args()

    if not 1 <= args.start <= 65535:
        parser.error("Start port must be between 1 and 65535")

    if not 1 <= args.end <= 65535:
        parser.error("End port must be between 1 and 65535")

    if args.start > args.end:
        parser.error("Start port must be lower than end port")

    print("=" * 50)
    print("TCP Port Scanner")
    print("=" * 50)

    print(f"Scanning {args.target} " f"ports {args.start}-{args.end}")

    start_time = time.perf_counter()

    results = scan_ports(args.target, args.start, args.end, args.threads, args.timeout)

    duration = time.perf_counter() - start_time

    print_results(args.target, results, duration)


if __name__ == "__main__":
    main()
