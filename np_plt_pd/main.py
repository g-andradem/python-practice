import numpy as np

# x = np.array([1, 2, 3, 4, 5])

def part_1():
    vector = np.array(
        [1, 2, 3]
    )

    print(vector.ndim) # 1

    array = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(array.ndim) # 2

    bigArray = np.array([
        [[1, 2, 3],[4, 5, 6],[7, 8, 9]],
        [[10, 11, 12],[13, 14, 15],[16, 17, 18]],
        [[19, 20, 21],[22, 23, 24],[25, 26, 27]]
    ])

    print(bigArray.ndim) # 3
    print(bigArray[0][0][0]) # 1
    print(bigArray[0][0][1]) # 2
    print(bigArray[0][1][0]) # 4
    print(bigArray[1][0][0]) # 10

def part_2():
    ...