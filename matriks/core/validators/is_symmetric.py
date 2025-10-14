def is_symmetric(matriks):
    # 1. Pastikan matriks persegi
    if matriks.jumlah_baris != matriks.jumlah_kolom:
        return False
    
    # 2. Periksa elemen (i,j) = (j,i)
    for i in range(matriks.jumlah_baris):
        for j in range(matriks.jumlah_kolom):
            if matriks.data[i][j] != matriks.data[j][i]:
                return False
    
    return True

