
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
    pass

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

    tableau = [[0.0] * length for _ in range(length)]
    for index in range(length):
        tableau[index][0] = points[index][1]

    for yIndex in range(1, length):
        for xIndex in range(length - yIndex):
            numerator = ((x - points[xIndex + yIndex][0]) * tableau[xIndex][yIndex - 1] -
                         (x - points[xIndex][0]) * tableau[xIndex + 1][yIndex - 1])
            denominator = (points[xIndex][0] - points[xIndex + yIndex][0])
            tableau[xIndex][yIndex] = numerator / denominator

    return tableau[0][length - 1]

def main():
    points = [[0,0], [1,0.84], [2,1], [3,0.14],[4,-0.76]]
    functions = {1: linear, 2: polynomial, 3: cubic_spline, 4: lagrange, 5: neville}
    choice = int(input("Choose the interpolation method:\n1 - linear\n2 - polynomial\n3 - cubic_spline\n4 - lagrange\n5 - neville\n"))
    print(functions[choice](points, 0.5))


if __name__ == "__main__":
    main()
