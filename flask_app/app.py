import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend non-GUI untuk server
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import io, base64
from regression.linear_regression import RegresiLinear

app = Flask(__name__)


# ========== FUNGSI HELPER UNTUK INTERPRETASI ==========
def get_r2_label(r2_value):
    """Return label berdasarkan nilai R²"""
    if r2_value > 0.95:
        return "SANGAT AKURAT! ✅"
    elif r2_value > 0.85:
        return "AKURAT! ✅"
    elif r2_value > 0.70:
        return "CUKUP BAIK 👍"
    else:
        return "PERLU PERBAIKAN ⚠️"


def get_mape_label(mape_value):
    """Return label berdasarkan nilai MAPE"""
    if mape_value < 5:
        return "model sangat reliable! 🎯"
    elif mape_value < 10:
        return "model reliable! ✅"
    elif mape_value < 20:
        return "model cukup baik 👍"
    else:
        return "perlu improvement ⚠️"


def create_advanced_visualization(y_actual, y_pred):
    """
    Visualisasi 3-panel untuk dataset besar:
    1. Density Heatmap (Hexbin)
    2. Scatter Plot dengan transparansi
    3. Residual Plot
    """
    # PENTING: Pastikan dimensi sama dan 1D
    y_actual = np.array(y_actual).flatten()
    y_pred = np.array(y_pred).flatten()
    
    # Validasi ukuran
    if len(y_actual) != len(y_pred):
        raise ValueError(f"Size mismatch: y_actual={len(y_actual)}, y_pred={len(y_pred)}")
    
    # Setup figure
    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize=(18, 5), dpi=100)
    
    # Hitung metrik evaluasi
    r2 = r2_score(y_actual, y_pred)
    rmse = np.sqrt(mean_squared_error(y_actual, y_pred))
    mae = mean_absolute_error(y_actual, y_pred)
    
    # Handle division by zero untuk MAPE
    mask = y_actual != 0
    if mask.sum() > 0:
        mape = np.mean(np.abs((y_actual[mask] - y_pred[mask]) / y_actual[mask])) * 100
    else:
        mape = 0.0
    
    # Nilai min-max untuk garis ideal
    min_val = min(y_actual.min(), y_pred.min())
    max_val = max(y_actual.max(), y_pred.max())
    
    # ========== PANEL 1: DENSITY HEATMAP ==========
    ax1 = plt.subplot(1, 3, 1)
    
    hexbin = ax1.hexbin(y_actual, y_pred, 
                       gridsize=35, 
                       cmap='YlOrRd',
                       mincnt=1,
                       edgecolors='black',
                       linewidths=0.2,
                       alpha=0.9)
    
    # Garis ideal
    ax1.plot([min_val, max_val], [min_val, max_val], 
            'b-', linewidth=3, alpha=0.8, label='Garis Ideal')
    
    # Colorbar
    cbar1 = plt.colorbar(hexbin, ax=ax1, pad=0.02)
    cbar1.set_label('Jumlah Data Points', fontsize=11, fontweight='bold')
    
    # Labels & title
    ax1.set_xlabel('Performance Index (Aktual)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Performance Index (Prediksi)', fontsize=12, fontweight='bold')
    ax1.set_title('Density Heatmap\n(Konsentrasi Data)', 
                 fontsize=13, fontweight='bold', pad=10)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.legend(loc='upper left', fontsize=10, framealpha=0.9)
    
    # ========== PANEL 2: SCATTER PLOT ==========
    ax2 = plt.subplot(1, 3, 2)
    
    scatter = ax2.scatter(y_actual, y_pred, 
                         c=y_actual,
                         cmap='plasma',
                         alpha=0.3,
                         s=20,
                         edgecolors='none',
                         rasterized=True)
    
    # Garis ideal
    ax2.plot([min_val, max_val], [min_val, max_val], 
            'r--', linewidth=3, alpha=0.8, label='Garis Ideal')
    
    # Colorbar
    cbar2 = plt.colorbar(scatter, ax=ax2, pad=0.02)
    cbar2.set_label('Nilai Aktual', fontsize=11, fontweight='bold')
    
    # Text box dengan metrik (posisi kanan bawah)
    textstr = f'R²    = {r2:.4f}\nRMSE  = {rmse:.3f}\nMAE   = {mae:.3f}\nMAPE  = {mape:.2f}%'
    props = dict(boxstyle='round,pad=0.6', 
                facecolor='lightblue', 
                alpha=0.85, 
                edgecolor='black', 
                linewidth=1.5)
    ax2.text(0.98, 0.02, textstr, 
            transform=ax2.transAxes, 
            fontsize=10,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=props,
            fontfamily='monospace',
            fontweight='bold')
    
    # Labels & title
    ax2.set_xlabel('Performance Index (Aktual)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Performance Index (Prediksi)', fontsize=12, fontweight='bold')
    ax2.set_title('Scatter Plot\n(Individual Points)', 
                 fontsize=13, fontweight='bold', pad=10)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.legend(loc='upper left', fontsize=10, framealpha=0.9)
    
    # ========== PANEL 3: RESIDUAL PLOT ==========
    ax3 = plt.subplot(1, 3, 3)
    
    residuals = y_actual - y_pred
    
    # Scatter residual
    ax3.scatter(y_pred, residuals, 
               alpha=0.3, 
               s=20, 
               c='coral', 
               edgecolors='none',
               rasterized=True)
    
    # Garis horizontal di y=0
    ax3.axhline(y=0, color='red', linestyle='--', linewidth=2, alpha=0.8)
    
    # Tambahkan batas +/- 2*std untuk outlier detection
    std_residual = np.std(residuals)
    ax3.axhline(y=2*std_residual, color='orange', linestyle=':', linewidth=1.5, alpha=0.7, label='+2σ')
    ax3.axhline(y=-2*std_residual, color='orange', linestyle=':', linewidth=1.5, alpha=0.7, label='-2σ')
    
    # Labels & title
    ax3.set_xlabel('Performance Index (Prediksi)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Residual (Aktual - Prediksi)', fontsize=12, fontweight='bold')
    ax3.set_title('Residual Plot\n(Error Distribution)', 
                 fontsize=13, fontweight='bold', pad=10)
    ax3.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, which='both')
    ax3.legend(loc='upper right', fontsize=9, framealpha=0.9)
    
    # ========== SUPER TITLE ==========
    fig.suptitle(f'Student Performance Prediction Model | R²={r2:.4f} | RMSE={rmse:.3f} | MAE={mae:.3f}', 
                fontsize=15, fontweight='bold', y=0.98)
    
    # Tight layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    return fig


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files['csv_file']
            
            # Baca CSV (dukung delimiter ; atau ,)
            df = pd.read_csv(file, sep=None, engine='python')
            
            print(f"✅ CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
            
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
            
            print(f"✅ X shape: {X.shape}, y shape: {y.shape}")
            
            # Latih model regresi
            model = RegresiLinear(X, y)
            theta = model.train()
            y_pred = model.predict(X)
            
            print(f"✅ Prediction done. y_pred shape: {y_pred.shape}")
            
            # PENTING: Pastikan y dan y_pred 1D dengan ukuran sama
            y = np.array(y).flatten()
            y_pred = np.array(y_pred).flatten()
            
            print(f"✅ After flatten - y: {y.shape}, y_pred: {y_pred.shape}")
            
            # Validasi ukuran
            if len(y) != len(y_pred):
                raise ValueError(f"❌ Size mismatch after prediction: y={len(y)}, y_pred={len(y_pred)}")
            
            # --- VISUALISASI 3-PANEL ---
            fig = create_advanced_visualization(y, y_pred)
            
            # Simpan ke buffer & encode base64
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            buf.seek(0)
            img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            buf.close()
            plt.close(fig)  # Tutup figure untuk hemat memori
            
            # Hitung metrik untuk ditampilkan
            r2 = r2_score(y, y_pred)
            rmse = np.sqrt(mean_squared_error(y, y_pred))
            mae = mean_absolute_error(y, y_pred)
            
            # Hitung MAPE
            mask = y != 0
            if mask.sum() > 0:
                mape = np.mean(np.abs((y[mask] - y_pred[mask]) / y[mask])) * 100
            else:
                mape = 0.0
            
            # Return template dengan variabel tambahan untuk interpretasi
            return render_template(
                'result.html',
                theta=theta.tolist() if isinstance(theta, np.ndarray) else theta,
                y_pred=y_pred.tolist(),
                img_data=img_base64,
                r2=f"{r2:.4f}",
                rmse=f"{rmse:.3f}",
                mae=f"{mae:.3f}",
                mape=f"{mape:.2f}",
                r2_percent=f"{r2*100:.2f}",        # Untuk interpretasi
                r2_label=get_r2_label(r2),          # Label R²
                mape_label=get_mape_label(mape)     # Label MAPE
            )
        
        except Exception as e:
            import traceback
            error_msg = traceback.format_exc()
            print(f"❌ ERROR: {error_msg}")
            return f"<h1>Error:</h1><pre>{error_msg}</pre>", 500
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
