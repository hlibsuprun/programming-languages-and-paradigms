from functools import reduce


def add_matrices(matrixA, matrixB):
    return [[matrixA[i][j] + matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]


def multiply_matrices(matrixA, matrixB):
    return [[sum(matrixA[i][k] * matrixB[k][j] for k in range(len(matrixB)))
             for j in range(len(matrixB[0]))] for i in range(len(matrixA))]


def combine_matrices(matrixA, matrixB, operation):
    if operation == 'add':
        return add_matrices(matrixA, matrixB)
    elif operation == 'multiply':
        return multiply_matrices(matrixA, matrixB)


def perform_reduction(matrices, operation):
    return reduce(lambda a, b: combine_matrices(a, b, operation), matrices)


matrices = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
result = perform_reduction(matrices, 'add')
print(result)
