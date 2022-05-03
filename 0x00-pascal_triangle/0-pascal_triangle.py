from random import triangular


def pascal_triangle(n):
    triangle=[]

    for rows in range(n):
        row = [None for _ in range(rows+1)]
        row[0], row[-1] = 1,1

        for j in range(1,len(row)-1):
            row[j] = triangle[rows-1][j-1] + triangle[rows-1][j]
        triangle.append(row)
    return triangle

print(pascal_triangle(5))