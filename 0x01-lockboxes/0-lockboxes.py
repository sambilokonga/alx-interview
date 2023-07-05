#!/usr/bin/python3
"""Script will unlock list of lists
n number of locked boxes
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
