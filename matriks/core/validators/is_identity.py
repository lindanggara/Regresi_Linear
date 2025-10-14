def is_identity(matriks):
    # 1. Pastikan matriks persegi
    if matriks.jumlah_baris != matriks.jumlah_kolom:
        return False
    
    # 2. Periksa elemen diagonal = 1, elemen lain = 0
    for i in range(matriks.jumlah_baris):
        for j in range(matriks.jumlah_kolom):
            if i == j and matriks.data[i][j] != 1:
                return False
            elif i != j and matriks.data[i][j] != 0:
                return False
    
    return True
