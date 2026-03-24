import numpy as np

if __name__ == "__main__":

    def vertor_dot(v1, v2):
        sum = 0
        for e1, e2 in zip(v1, v2):
            sum += e1 * e2
        return sum

    v1 = np.random.rand(5)
    v2 = np.random.rand(5)
    print(v1)
    print(v2)
    sum = vertor_dot(v1, v2)

    print(sum)
