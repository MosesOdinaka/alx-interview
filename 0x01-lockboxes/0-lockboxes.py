#!/usr/bin/python3
"""
This function checks if all boxes can be opened.
"""

def canUnlockAll(boxList):
    """
    This function checks if all boxes in the list can be opened.
    :param boxList: List of boxes
    :return: Boolean value indicating if all boxes can be opened
    """

    # Check if boxList is a list
    if not isinstance(boxList, list):
        return False

    # Check if boxList is empty
    if not boxList:
        return False

    # Initialize list of keys with the first box key
    availableKeys = [0]

    # Iterate over the available keys
    for keyIndex in availableKeys:
        # Iterate over keys in the current box
        for key in boxList[keyIndex]:
            # Check conditions before adding the key
            if (key not in availableKeys and key != keyIndex and 
                key < len(boxList) and key != 0):
                availableKeys.append(key)

    # Check if all boxes can be opened
    return len(availableKeys) == len(boxList)
