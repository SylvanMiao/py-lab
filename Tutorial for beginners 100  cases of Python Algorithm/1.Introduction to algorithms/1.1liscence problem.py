if __name__ == "__main__":
    for i in range(10):
        for j in range(10):
            if i != j:
                k = 1000 * i + 100 * i + 10 * j + j
                for temp in range(31, 100):
                    if k == temp * temp:
                        print(k)
