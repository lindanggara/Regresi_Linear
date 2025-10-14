# app/main_sparse.py

import sys, os
# Pastikan Python tahu path root project
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from matriks.core.matrix import Matrix
from matriks.core.exporters.csv_exporter import export_to_csv
from matriks.core.exporters.json_exporter import export_to_json

if __name__ == "__main__":
    # Buat objek matriks contoh
    matriks_demo = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Tentukan folder output
    output_dir = os.path.join(os.path.dirname(__file__), "../data/output")
    os.makedirs(output_dir, exist_ok=True)

    # Ekspor ke CSV
    path_csv = os.path.join(output_dir, "matriks_output.csv")
    print("📁 Mengekspor matriks ke format CSV...")
    export_to_csv(matriks_demo, path_csv)

    # Ekspor ke JSON
    path_json = os.path.join(output_dir, "matriks_output.json")
    print("\n📁 Mengekspor matriks ke format JSON...")
    export_to_json(matriks_demo, path_json)

    print("\n✅ Semua ekspor selesai tanpa error.")
