import json

def export_to_json(matriks, nama_file):
    # ambil data matriks
    data = matriks.data  # atau matriks.matrix sesuai atribut Matrix
    with open(nama_file, "w") as f:
        json.dump(data, f)
    print(f"Matriks berhasil diekspor ke {nama_file} dalam format JSON")
