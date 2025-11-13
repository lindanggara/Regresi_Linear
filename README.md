# 📊 **Student Performance Prediction (Regresi Linear dengan Visualisasi Interaktif)**

Proyek ini adalah aplikasi **Flask berbasis web** yang digunakan untuk **melatih model regresi linear** dan **menampilkan hasil prediksi dalam bentuk visual interaktif**.
Pengguna cukup mengunggah file CSV (dataset), dan sistem akan secara otomatis:

* Membersihkan data (konversi kategori menjadi numerik)
* Melatih model regresi linear
* Menghitung metrik evaluasi (R², RMSE, MAE, MAPE)
* Menampilkan **3 visualisasi interaktif** hasil prediksi

---

## ⚙️ **Fitur Utama**

✅ Upload file CSV secara langsung
✅ Otomatis mendeteksi delimiter (`,` atau `;`)
✅ Visualisasi hasil regresi dalam 3 panel:

1. **Density Heatmap** – Menunjukkan area konsentrasi data
2. **Scatter Plot** – Perbandingan nilai aktual vs prediksi
3. **Residual Plot** – Distribusi error prediksi

✅ Menampilkan metrik performa:

* **R² (Koefisien Determinasi)**
* **RMSE (Root Mean Squared Error)**
* **MAE (Mean Absolute Error)**
* **MAPE (Mean Absolute Percentage Error)**

✅ Interpretasi otomatis hasil model
✅ Tombol download visualisasi (.png)
✅ Tampilan sederhana dan responsif

---

## 🧰 **Struktur Folder**

```
project/
│
├── flask_app/
│   ├── app.py                # File utama Flask
│   ├── templates/
│   │   ├── index.html        # Halaman upload dataset
│   │   └── result.html       # Halaman hasil prediksi & visualisasi
│   └── static/               # Folder opsional untuk CSS/JS tambahan
│
├── regression/
│   └── linear_regression.py  # Implementasi Regresi Linear (dengan numpy)
│
└── requirements.txt          # Daftar dependensi Python
```

---

## 🧪 **Instalasi & Menjalankan Aplikasi**

### 1️⃣ Clone repository

```bash
git clone https://github.com/<username>/<nama-repo>.git
cd <nama-repo>
```

### 2️⃣ Buat dan aktifkan virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Mac / Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install dependensi

```bash
pip install -r requirements.txt
```

Atau manual:

```bash
pip install flask numpy pandas scikit-learn matplotlib
```

### 4️⃣ Jalankan aplikasi Flask

```bash
python flask_app/app.py
```

Buka di browser:

```
http://127.0.0.1:5000/
```

---

## 📈 **Cara Menggunakan**

1. Jalankan aplikasi Flask.
2. Buka browser dan masuk ke halaman utama.
3. Upload file CSV dengan struktur seperti contoh berikut:

| StudyHours | Attendance | PerformanceIndex |
| ---------- | ---------- | ---------------- |
| 6.5        | 85         | 78               |
| 8.0        | 90         | 88               |
| 4.5        | 70         | 65               |

4. Klik **Upload** → sistem akan otomatis melatih model dan menampilkan hasil visualisasi.
5. Lihat:

   * Nilai **θ (parameter model)**
   * **Prediksi tiap data**
   * **Grafik interaktif**
   * Interpretasi otomatis performa model

---

## 🧮 **Contoh Hasil Output**

### 🔢 *Metrik Model*

| Metrik   | Nilai  | Interpretasi                                    |
| -------- | ------ | ----------------------------------------------- |
| **R²**   | 0.9231 | Model akurat (menjelaskan 92.31% variasi data)  |
| **RMSE** | 4.312  | Error rata-rata ±4.3 poin dari nilai sebenarnya |
| **MAE**  | 3.520  | Error absolut rata-rata 3.5 poin                |
| **MAPE** | 5.62%  | Model reliable! ✅                               |

### 📊 *Visualisasi Otomatis*

1. **Density Heatmap:** area merah = data banyak dan model stabil
2. **Scatter Plot:** titik-titik mendekati garis ideal → prediksi akurat
3. **Residual Plot:** sebaran acak di sekitar garis 0 → model tidak bias

---

## 💡 **Interpretasi Cepat**

* **R² tinggi (>0.85)** → model mampu menjelaskan sebagian besar variasi target.
* **RMSE & MAE rendah** → prediksi model mendekati nilai aktual.
* **MAPE < 10%** → model cukup atau sangat reliable.
* **Residual acak** → model tidak mengalami bias sistematik.

---

## 📥 **Contoh Dataset**

Kamu bisa mengunggah dataset seperti:

```csv
StudyHours,Attendance,PerformanceIndex
6.5,85,78
8.0,90,88
4.5,70,65
9.1,92,95
```

---

## 🖼️ **Hasil Visualisasi**

Begitu di-upload, kamu akan melihat tampilan seperti ini:

* Metrik evaluasi lengkap (R², RMSE, MAE, MAPE)
* Interpretasi otomatis dalam kotak kuning
* Gambar 3 panel hasil prediksi
* Tombol untuk **Download Visualisasi**
* Tabel nilai **θ (parameter)** dan **y_pred (hasil prediksi)**

---

## 👨‍💻 **Dibangun Dengan**

* [Python 3.x](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [NumPy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [scikit-learn](https://scikit-learn.org/)
* [Matplotlib](https://matplotlib.org/)

