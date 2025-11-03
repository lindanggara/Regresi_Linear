import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import numpy as np
from transpose import transpose_matrix
from inverse import inverse_matrix
from import_csv import import_matrix_from_csv

if __name__ == "__main__":
    A = np.array([[2, 3],
                  [1, 4]])

    print("=== Matriks A ===")
    print(A)

    print("\n=== Transpose A ===")
    print(transpose_matrix(A))

    print("\n=== Invers A ===")
    print(inverse_matrix(A))

    print("\n=== Import dari CSV (contoh file hasil_perkalian.csv) ===")
    try:
        matrix_csv = import_matrix_from_csv("../../data/output/hasil_perkalian.csv", delimiter=',')
        print(matrix_csv)
    except Exception as e:
        print(f"Gagal import CSV: {e}")
