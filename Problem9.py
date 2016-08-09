def main():
    n = 1000
    topNumToCheck = 998
    for c in range(topNumToCheck, 3, -1):
        for b in range(c, 3, -1):
            for a in range(b, 3, -1):
                if isCorrectPythagoreanTriplet(a, b, c, n):
                    productSum = a * b * c
                    print(str(a) + "*" + str(b) + "*" +
                          str(c) + "=" + str(productSum))
                    return


def isCorrectPythagoreanTriplet(a, b, c, n):
    if (a + b + c) == n:
        return (a**2 + b**2) == c**2

if __name__ == "__main__":
    main()
