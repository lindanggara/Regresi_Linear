import numpy as np

def inverse_matrix(matrix):
    """
    Mengembalikan invers dari matriks persegi.
    """
    try:
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matriks harus persegi untuk dihitung inversenya.")
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Matriks tidak memiliki invers (determinannya 0).")
