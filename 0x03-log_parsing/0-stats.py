#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
num_lines_read = 0
status_code_map = {}
file_size = 0


def print_stats():
    """Function to print the current statistics."""
    print("File size: {}".format(file_size))
    for stat, count in sorted(status_code_map.items()):
        print("{}: {}".format(stat, count))


try:
    for line in sys.stdin:
        line_token = line.split()
        try:
            f_size = int(line_token[-1])
            file_size += f_size
            status_code = int(line_token[-2])
            if status_code in status_codes:
                if status_code in status_code_map:
                    status_code_map[status_code] += 1
                else:
                    status_code_map[status_code] = 1
        except ValueError:
            pass
        num_lines_read += 1
        if num_lines_read % 10 == 0:
            print_stats()

    if (num_lines_read == 0) or (num_lines_read % 10 != 0):
        print_stats()

except (KeyboardInterrupt):
    print_stats()
