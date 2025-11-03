import numpy as np

def transpose_matrix(matrix):
    """
    Mengembalikan transpose dari matriks.
    """
    try:
        return np.transpose(matrix)
    except Exception as e:
        raise ValueError(f"Gagal melakukan transpose: {e}")
