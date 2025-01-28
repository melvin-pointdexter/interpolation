
def linear():
    pass

def polynomial():
    pass

def cubic_spline():
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

def neville():
    pass

def main():
    points = [[0,0], [1,0.84], [2,1], [3,0.14],[4,-0.76]]
    print(lagrange(points, 0.5))


if __name__ == "__main__":
    main()
