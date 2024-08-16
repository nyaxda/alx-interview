#!/usr/bin/python3
"""log parsing module"""
import sys
import re
import signal

pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
    r'"GET /[^ ]+ HTTP/1.1" \d{3} \d+$'
)
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
status_code_counts = {code: 0 for code in valid_status_codes}

total_size = 0
line_count = 0


def print_stats():
    """prints the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interruption which is CTRL + C"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
while True:
    try:
        line = sys.stdin.readline()  # it reads input line by line
        if not line:
            break
        line = line.strip()
        if pattern.match(line):
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size
            line_count += 1

            if status_code in valid_status_codes:
                status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

# in case of no interruption
print_stats()
