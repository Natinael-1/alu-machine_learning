#!/usr/bin/env python3
"""Module for calculating the definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if (matrix.ndim != 2 or matrix.size == 0
            or matrix.shape[0] != matrix.shape[1]):
        return None
    if not np.allclose(matrix, matrix.T):
        return None

    w = np.linalg.eigvalsh(matrix)
    tol = 1e-10
    n = len(w)
    pos = np.sum(w > tol)
    neg = np.sum(w < -tol)

    if pos == n:
        return "Positive definite"
    if neg == n:
        return "Negative definite"
    if neg == 0:
        return "Positive semi-definite"
    if pos == 0:
        return "Negative semi-definite"
    return "Indefinite"

