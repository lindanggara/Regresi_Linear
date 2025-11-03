import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io, base64
from regression.linear_regression import RegresiLinear

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['csv_file']

        # Baca CSV (dukung delimiter ; atau ,)
        df = pd.read_csv(file, sep=None, engine='python')

        # Bersihkan kolom non-numerik (misal Yes/No)
        for col in df.columns:
            if df[col].dtype == 'object':
                # Coba ubah Yes/No menjadi 1/0
                df[col] = df[col].map({'Yes': 1, 'No': 0})
                # Jika masih string lainnya, ubah pakai label encoding sederhana
                if df[col].dtype == 'object':
                    df[col] = pd.factorize(df[col])[0]

        # Pisahkan fitur dan target (kolom terakhir)
        X = df.iloc[:, :-1].values.astype(float)
        y = df.iloc[:, -1].values.astype(float)

        # Latih model regresi
        model = RegresiLinear(X, y)
        theta = model.train()
        y_pred = model.predict(X)

        # --- VISUALISASI HASIL ---
        plt.figure(figsize=(6, 4))
        plt.scatter(y, y_pred, color='blue', label='Prediksi vs Aktual')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='Garis Ideal (y = y_pred)')
        plt.xlabel('Aktual')
        plt.ylabel('Prediksi')
        plt.title('Visualisasi Hasil Regresi Linear')
        plt.legend()
        plt.tight_layout()

        # Simpan ke buffer & encode base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        return render_template(
            'result.html',
            theta=theta.tolist() if isinstance(theta, np.ndarray) else theta,
            y_pred=y_pred.tolist(),
            img_data=img_base64
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
