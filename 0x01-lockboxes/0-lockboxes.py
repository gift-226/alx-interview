#!/usr/bin/python3
"""Unlocks list of lists"""


def canUnlockAll(boxes):
    """Takes a list of lists and the content of the list will unlock other lists

    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
