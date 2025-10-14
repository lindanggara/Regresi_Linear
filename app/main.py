# app/main.py

import sys, os
# Tambahkan path root project agar bisa import package matriks dengan benar
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from matriks.core.matrix import Matrix
from matriks.core.operations.adder import add_matrices
from matriks.core.operations.multiplier import multiply_matrices
from matriks.core.utilities.formatter import to_string
from matriks.core.exporters.csv_exporter import export_to_csv

if __name__ == "__main__":
    matriks_a = Matrix([[1, 2], [3, 4]])
    matriks_b = Matrix([[5, 6], [7, 8]])

    print("=== HASIL PENJUMLAHAN ===")
    hasil_penjumlahan = add_matrices(matriks_a, matriks_b)
    print(to_string(hasil_penjumlahan))

    print("\n=== HASIL PERKALIAN ===")
    hasil_perkalian = multiply_matrices(matriks_a, matriks_b)
    print(to_string(hasil_perkalian))

    # Simpan hasil ke file CSV
    output_dir = os.path.join(os.path.dirname(__file__), "../data/output")
    os.makedirs(output_dir, exist_ok=True)

    path_penjumlahan = os.path.join(output_dir, "hasil_penjumlahan.csv")
    path_perkalian = os.path.join(output_dir, "hasil_perkalian.csv")

    print(f"\n📁 Menyimpan hasil penjumlahan ke: {path_penjumlahan}")
    export_to_csv(hasil_penjumlahan, path_penjumlahan)

    print(f"📁 Menyimpan hasil perkalian ke: {path_perkalian}")
    export_to_csv(hasil_perkalian, path_perkalian)

    print("\n✅ Eksekusi selesai tanpa error.")
