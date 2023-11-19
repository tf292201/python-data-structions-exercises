def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:
    """
    total_sum = 0
    for i in range(len(matrix)):
        total_sum += matrix[i][i]
        total_sum += matrix[i][len(matrix)-i-1]
    return total_sum


print(sum_up_diagonals([
    [1,   2],
    [30, 40],
]))
print(sum_up_diagonals([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]))
