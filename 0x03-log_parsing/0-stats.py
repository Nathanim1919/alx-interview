#!/usr/bin/python3
"""Log parsing"""


import sys


# Define a dictionary to store the status codes and their count
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_sizes = []


try:
    # Read the standard input line by line
    for i, line in enumerate(sys.stdin, 1):
        # Parse the line and extract the status code and file size

        data = line.split()
        if len(data) >= 7:
            status_code = int(data[-2])
            file_size = int(data[-1])

            # If the status code is in the dictionary, increment its count
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                pass

            # Append the file size to the list
            file_sizes.append(file_size)

        # Print statistics after every 10 lines
        if i % 10 == 0:
            total_size = sum(file_sizes)
            print(f"File size: {total_size}")
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle the Keyboard Interrupt
    total_size = sum(file_sizes)
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
