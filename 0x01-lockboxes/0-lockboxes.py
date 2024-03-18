#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""


def canUnlockAll(box_list):
    """
    Function to check if all boxes in the list can be opened.

    Parameters:
    box_list (list): List of boxes

    Returns:
    bool: True if all boxes can be opened, False otherwise
    """

    # Check if box_list is a list
    if not isinstance(box_list, list):
        return False

    # Check if box_list is empty
    if not box_list:
        return False

    # Initialize list of keys with the first box key
    available_keys = [0]

    # Iterate over the available keys
    for key_index in available_keys:
        # Iterate over keys in the current box
        for key in box_list[key_index]:
            # Check conditions before adding the key
            if (key not in available_keys and key != key_index and
               key < len(box_list) and key != 0):
                available_keys.append(key)

    # Check if all boxes can be opened
    return len(available_keys) == len(box_list)
