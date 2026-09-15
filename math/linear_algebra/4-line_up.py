#!/usr/bin/env python3
"""Module that returns the transpose of a 2D matrix."""

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
