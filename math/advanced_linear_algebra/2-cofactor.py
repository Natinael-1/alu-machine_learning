#!/usr/bin/env python3

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(n):
        sub = [row[:j] + row[j +1:] for row in matrix[1:]]
        det += (-1) ** j * matrix[0][j] * determinant(sub)
    return det

def minor(matrix):
    n = len(matrix)
    if n == 1:
        return [[1]]
    return [[determinant([row[:j] + row[j + 1:]
                            for r, row in enumerate(matrix) if r != i])
                        for j in range(n)] for i in range(n)]

def cofactor(matrix):
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    m = minor(matrix)
    return [[(-1) ** (i + j) * m[i][j] for j in range(n)] for i in range(n)]
