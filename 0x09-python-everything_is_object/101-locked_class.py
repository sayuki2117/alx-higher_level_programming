#!/usr/bin/python3
# 101-locked_class.py
# @sayuki2117

"""Locked Class Defination."""

class LockedClass:
    """This class creates instance
    only if is called first_name
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """This method initialize the object."""
        if hasattr(self, first_name):
            self.first_name = first_name
