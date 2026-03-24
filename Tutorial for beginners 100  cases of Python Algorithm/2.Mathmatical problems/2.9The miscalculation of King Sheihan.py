# 等比数列求和
if __name__ == "__main__":
    sum = 1
    for i in range(0, 64):
        sum += sum
        print(sum)
