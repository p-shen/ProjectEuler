class retClass:
    maxNum = 0
    x = 0
    y = 0

def solution():
    ret = retClass()
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            num = i*j
            str1 = str(num)
            str2 = str1[::-1] #reverse string
            if str1 == str2 and num > ret.maxNum:
                ret.maxNum = num
                ret.x = i
                ret.y = j

    return ret

maxVar = solution()
print(str(maxVar.x) + " " + str(maxVar.y) + " " + str(maxVar.maxNum))
