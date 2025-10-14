# operations/determinant.py

def find_determinant(matrix):
    """
    Menghitung determinan matriks (contoh sederhana untuk 2x2).
    """
    if matrix.rows != matrix.cols:
        raise ValueError("Determinant hanya bisa dihitung untuk matriks persegi.")

    if matrix.rows == 2:
        return matrix.data[0][0] * matrix.data[1][1] - matrix.data[0][1] * matrix.data[1][0]

    # TODO: Implementasi untuk ukuran > 2
    raise NotImplementedError("Determinant untuk ukuran > 2 belum diimplementasikan.")
