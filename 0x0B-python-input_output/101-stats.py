import sys

def print_metrics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

def process_logs():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip, _, _, status_code, file_size = line.strip().split(" ")[0:5]
            total_size += int(file_size)

            if status_code not in status_codes:
                status_codes[status_code] = 0
            status_codes[status_code] += 1

            if i % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

process_logs()
