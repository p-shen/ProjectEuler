def sumOfSquares(startingNum, endingNum):
    ret = 0
    for i in range(startingNum, endingNum):
        ret += i ** 2
    return ret


def sumSquared(startingNum, endingNum):
    ret = 0
    for i in range(startingNum, endingNum):
        ret += i
    ret = ret ** 2
    return ret


def main():
    # first 100 natural numbers is 1 to 101 inclusive
    startingNum = 1
    endingNum = 101
    sumSquaredNum = sumSquared(startingNum, endingNum)
    sumOfSquaresNum = sumOfSquares(startingNum, endingNum)
    diff = sumSquaredNum - sumOfSquaresNum
    print(str(sumSquaredNum) + " - " + str(sumOfSquaresNum) + " = " + str(diff))


if __name__ == "__main__":
    main()
