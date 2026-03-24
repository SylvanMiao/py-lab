if __name__ == "__main__":
    totalmoney = 0
    for i in range(0, 5):
        totalmoney = (1000 + totalmoney) / (1 + 12 * 0.0063)
    print("%.3f" % totalmoney)
