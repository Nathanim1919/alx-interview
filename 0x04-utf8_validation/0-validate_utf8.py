#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if byte >> 7 == 0:  # Single-byte character
                continue
            elif byte >> 5 == 0b110:  # Two-byte character
                num_bytes_to_follow = 1
            elif byte >> 4 == 0b1110:  # Three-byte character
                num_bytes_to_follow = 2
            elif byte >> 3 == 0b11110:  # Four-byte character
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
