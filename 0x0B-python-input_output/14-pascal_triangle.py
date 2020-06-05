#!/usr/bin/python3
''' a list of lists of integers module'''


def pascal_triangle(n):
    ''' a list of lists of integers function'''
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(last[j] + last[j - 1])
        last = row
        triangle.append(row)
    return triangle
