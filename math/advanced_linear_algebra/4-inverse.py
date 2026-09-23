#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a square matrix"""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(n):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += (-1) ** j * matrix[0][j] * determinant(sub)
    return det


def minor(matrix):
    """Calculates the minor matrix of a square matrix"""
    n = len(matrix)
    if n == 1:
        return [[1]]
    minors = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            sub = []
            for r, row in enumerate(matrix):
                if r == i:
                    continue
                sub.append(row[:j] + row[j + 1:])
            row_minors.append(determinant(sub))
        minors.append(row_minors)
    return minors


def cofactor(matrix):
    """Calculates the cofactor matrix of a square matrix"""
    n = len(matrix)
    m = minor(matrix)
    cof = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            row_cof.append((-1) ** (i + j) * m[i][j])
        cof.append(row_cof)
    return cof


def adjugate(matrix):
    """Calculates the adjugate matrix of a square matrix"""
    n = len(matrix)
    c = cofactor(matrix)
    adj = []
    for i in range(n):
        new_row = []
        for j in range(n):
            new_row.append(c[j][i])
        adj.append(new_row)
    return adj


def inverse(matrix):
    """Calculates the inverse of a matrix, or None if it is singular"""
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    det = determinant(matrix)
    if det == 0:
        return None
    adj = adjugate(matrix)
    inv = []
    for i in range(n):
        row_inv = []
        for j in range(n):
            row_inv.append(adj[i][j] / det)
        inv.append(row_inv)
    return inv

