#!/usr/bin/python3

def pascal_triangle(n):
    """return the pascal triangle with number of n row

    Args:
        n (int): args n of int type passed into the function

    Returns:
        int: int using a nCk (n Combination k) formulae
    """
    triangle=[]

    for rows in range(n):
        row = [None for _ in range(rows+1)]
        row[0], row[-1] = 1,1

        for j in range(1,len(row)-1):
            row[j] = triangle[rows-1][j-1] + triangle[rows-1][j]
        triangle.append(row)
    return triangle

print(pascal_triangle(5))