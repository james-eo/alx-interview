#!/usr/bin/env python3
"""This module contains the implementation of log parsing"""
import sys
import signal

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Function to print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handle_interrupt(signum, frame):
    """Function to handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 9:
            continue

        ip = parts[0]
        date = parts[3][1:]
        request = parts[5][1:]
        status_code = int(parts[8])
        file_size = int(parts[9])

        total_file_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue

print_stats()
