#!/usr/bin/python3
"""Module for lockboxes"""


def canUnlockAll(boxes):
    """
    function to unlock boxes
    Args:
        boxes: list of lists
    Return: True or False
    """
    # holds the boxes to be processed
    stack = []

    # a set to keep track of opened boxes
    opened_boxes = set()
    stack.append(boxes[0])
    opened_boxes.add(0)

    while stack:
        current_box = stack.pop()
        for key in current_box:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(boxes[key])

    return len(opened_boxes) == len(boxes)
