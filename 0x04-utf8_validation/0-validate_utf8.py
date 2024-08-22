#!/usr/bin/python3
"""Module for utf-8 validation"""


def validUTF8(data):
    """module for utf-8 validation"""
    # checking if data is valid
    if data is None or len(data) == 0:
        return False
    filtered_data = []
    # filtering the least significant 8 bits
    for i in range(len(data)):
        filtered_data.append(data[i] & 0xFF)

    # converting them to binary equivalents:
    for i in range(len(filtered_data)):
        filtered_data[i] = bin(filtered_data[i])[2:].zfill(8)

    # determining the byte type
    i = 0
    while i < len(filtered_data):
        # checking if the length is > 8
        if len(filtered_data[i]) != 8:
            return False

        # utf-8 validation:
        # for a 4-byte sequence
        if filtered_data[i][:5] == '11110':
            if i + 3 >= len(filtered_data):
                return False
            if (filtered_data[i + 1][:2] != '10' or
                    filtered_data[i + 2][:2] != '10' or
                    filtered_data[i + 3][:2] != '10'):
                return False
            i += 4
            continue

        # for a 3-byte sequence
        elif filtered_data[i][:4] == '1110':
            if i + 2 >= len(filtered_data):
                return False
            if (filtered_data[i + 1][:2] != '10' or
                    filtered_data[i + 2][:2] != '10'):
                return False
            i += 3
            continue

        # for a 2-byte sequence
        elif filtered_data[i][:3] == '110':
            if i + 1 >= len(filtered_data):
                return False
            if filtered_data[i + 1][:2] != '10':
                return False
            i += 2
            continue

        # for a 1-byte sequence
        elif filtered_data[i][:1] == '0':
            i += 1
            continue
        # if none of the above conditions match, invalid sequence
        return False

    return True
