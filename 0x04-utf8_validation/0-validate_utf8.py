#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding
    """
    num_bytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for i in data:
        byte = 1 << 7
        if num_bytes == 0:
            while byte & i:
                num_bytes += 1
                byte = byte >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (i & byte1 and not (i & byte2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
