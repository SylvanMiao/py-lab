# print 所有n以内的平方具有对称性质的数
if __name__ == "__main__":
    n = int(input())

    for i in range(0, n + 1):
        square = i * i
        a = square
        j = 0
        value = 1
        negasquare = 0
        result = []
        negaresult = []
        posiresult = []
        while square != 0:
            result.append(square % 10)
            square //= 10
            j += 1
        # think the code below carefully
        while j > 0:
            negasquare += result[j - 1] * value
            value *= 10
            j -= 1
        for w in range(0, len(result)):
            posiresult.append(result[w])
        result.reverse()
        for t in range(0, len(result)):
            negaresult.append(result[t])

        """ if negaresult == posiresult:
            print(i, a) """
        if a == negasquare:
            print(i, a)
