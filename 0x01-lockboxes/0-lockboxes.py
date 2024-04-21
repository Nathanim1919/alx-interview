#!/usr/bin/python3
"""we have a list of boxes, each box is
 numbered sequentially from 0 to n - 1
   and each box may contain keys to other boxes."""


def canUnlockAll(boxes):
    """a Function, that return True if all boxs can be opened else False"""

    unlocked = [0]  # The first box is given open
    keys = boxes[0]  # Start with keys from the first box

    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    else:
        while len(keys) > 0:
            new_keys = []
            for key in keys:
                if key not in unlocked:
                    unlocked.append(key)
                    new_keys += boxes[key]
            keys = new_keys

    return len(unlocked) == len(boxes)
