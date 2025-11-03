import numpy as np
import pandas as pd

def import_matrix_from_csv(file_path, delimiter=','):
    """
    Mengimpor matriks dari file CSV.
    """
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        return df.to_numpy(dtype=float)
    except Exception as e:
        raise ValueError(f"Gagal membaca file CSV: {e}")
