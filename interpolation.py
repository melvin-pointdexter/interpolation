
def linear(points, x):
    for index in range(len(points) - 1):
        x1, y1 = points[index]
        x2, y2 = points[index + 1]
        if x1 <= x <= x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

    # else, do extrapolation
    if x < points[0][0]:
        x1, y1 = points[0]
        x2, y2 = points[1]
    else:
        x1, y1 = points[-2]
        x2, y2 = points[-1]
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

def polynomial(points, x):
    pass

def cubic_spline(points, x):
    length = len(points)
    h = [points[i + 1][0] - points[i][0] for i in range(length - 1)]

    # calculate the alpha
    alpha = [0] * (length - 1)
    for i in range(1, length - 1):
        alpha[i] = (3 / h[i]) * (points[i + 1][1] - points[i][1]) - (3 / h[i - 1]) * (points[i][1] - points[i - 1][1])

    # Tridiagonal system arrays
    one = [1] * length
    second = [0] * length
    third = [0] * length

    for i in range(1, length - 1):
        one[i] = 2 * (points[i + 1][0] - points[i - 1][0]) - h[i - 1] * second[i - 1]
        second[i] = h[i] / one[i]
        third[i] = (alpha[i] - h[i - 1] * third[i - 1]) / one[i]

    # Back-substitution
    c = [0] * length
    b = [0] * (length - 1)
    d = [0] * (length - 1)

    for j in range(length - 2, -1, -1):
        c[j] = third[j] - second[j] * c[j + 1]
        b[j] = ((points[j + 1][1] - points[j][1]) / h[j]) - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Find interval for x
    i = 0
    if x < points[0][0]:
        i = 0
    elif x > points[-1][0]:
        i = n - 2
    else:
        for j in range(length - 1):
            if points[j][0] <= x <= points[j + 1][0]:
                i = j
                break

    dx = x - points[i][0]
    return points[i][1] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

def lagrange(points, x):
    length = len(points)
    result = 0.0
    
    for i in range(length):
        term = points[i][1]
        for j in range(length):
            if i != j:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
        result += term
    return result

def neville(points, x):
    length = len(points)

    table = [[0.0] * length for _ in range(length)]
    for index in range(length):
        table[index][0] = points[index][1]

    for yIndex in range(1, length):
        for xIndex in range(length - yIndex):
            numerator = ((x - points[xIndex + yIndex][0]) * table[xIndex][yIndex - 1] -
                         (x - points[xIndex][0]) * table[xIndex + 1][yIndex - 1])
            denominator = (points[xIndex][0] - points[xIndex + yIndex][0])
            table[xIndex][yIndex] = numerator / denominator

    return table[0][length - 1]

def main():
    points = [[0,0], [1,1.23], [2,0.91], [3,-0.51],[4,-0.1],[5,0.23],[6,2.11]]
    functions = {1: linear, 2: polynomial, 3: cubic_spline, 4: lagrange, 5: neville}
    choice = int(input("Choose the interpolation method:\n1 - linear\n2 - polynomial\n3 - cubic_spline\n4 - lagrange\n5 - neville\n"))
    print(functions[choice](points, 0.5))


if __name__ == "__main__":
    main()
