import numpy as np
import pandas as pd
from sklearn.metrics import euclidean_distances


def transform_co_occurrence_into_distance(co_occurrence):
    result = []


if __name__ == '__main__':

    image = (np.random.rand(20, 20) * 10).astype(int)

    print('image')
    for row in image:
        print(row)
    # [print(row) for row in image]

    result_dict = {digit: {other_digit: 0 for other_digit in range(10)} for digit in range(10)}
    for row in image:
        prev_digit = None
        for digit in row:
            if prev_digit is not None:
                result_dict[prev_digit][digit] += 1
            prev_digit = digit

    print('co-occurrence matrix')
    for row in result_dict.items():
        print(row)
    # [print(row) for row in result_dict.items()]

    co_occurrence_matrix = pd.DataFrame(result_dict)

    print('co-occurrence matrix as DF')
    print(co_occurrence_matrix)

    print('distance matrix')
    result_distance_dict = {str(x)+str(y): {str(z)+str(h): abs(co_occurrence_matrix.loc[x, y] - co_occurrence_matrix.loc[z, h]) for z in range(10) for h in range(10)} for x in range(10) for y in range(10)}
    distance_matrix = pd.DataFrame(result_distance_dict)

    print(distance_matrix)

    print('Distance matrix 2')
    print(euclidean_distances(co_occurrence_matrix))


