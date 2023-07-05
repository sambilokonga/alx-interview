#!/usr/bin/python3
"""Script will unlock list of lists"""

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # First box is unlocked

    # Use a stack to keep track of boxes to visit
    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
