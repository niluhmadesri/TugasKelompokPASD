
# House Price Prediction API

> Praktikum Perancangan Aplikasi Sains Data — Kelompok 2 | Kelas DS-04-02

API berbasis FastAPI untuk memprediksi harga rumah menggunakan model Machine Learning (Random Forest Regressor) yang dilatih pada dataset California Housing dari scikit-learn.

---

## Anggota Kelompok

| No | Nama Lengkap | NIM |
|----|--------------|-----|
| 1 | Ni Luh Made Sri Utami Pradnyandari | 103102400055 |
| 2 | Safa Ayu Artanti | 103102430004 |

---

## Struktur File

TugasKelompokPASD/

├── predictor.py        # Modul load model, preprocessing, dan inferensi

├── main.py             # Web Service FastAPI (endpoint /predict)

├── deployment.ipynb    # Notebook Google Colab (training + deployment)

├── README.md           # Dokumentasi proyek

└── .gitignore          # Exclude file model (.joblib)

> ⚠️ File `house_price_model.joblib` tidak disertakan karena ukurannya melebihi batas GitHub (>100MB). Generate ulang dengan menjalankan Cell 1 di `deployment.ipynb`.

---

## Instalasi Dependencies

Jalankan perintah berikut untuk menginstall semua library yang dibutuhkan:

```bash
pip install fastapi uvicorn pyngrok scikit-learn joblib numpy
```

---

## Cara Menjalankan

### 1. Generate Model
Jalankan Cell 1 di `deployment.ipynb` untuk melatih dan menyimpan model:
```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

housing = fetch_california_housing()
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, '/content/house_price_model.joblib')
```

### 2. Jalankan Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. Akses Dokumentasi API
Buka browser dan akses: http://localhost:8000/docs

---

## Endpoint

### GET /
Mengecek apakah server berjalan.

**Response:**
```json
{"message": "House Price Prediction API is running!"}
```

### POST /predict
Menerima data rumah dalam format JSON dan mengembalikan prediksi harga.

---

## Deskripsi Fitur Input

| Fitur | Deskripsi | Tipe |
|-------|-----------|------|
| MedInc | Median pendapatan rumah tangga di blok tersebut | float |
| HouseAge | Usia rata-rata rumah di blok tersebut | float |
| AveRooms | Rata-rata jumlah ruangan per rumah tangga | float |
| AveBedrms | Rata-rata jumlah kamar tidur per rumah tangga | float |
| Population | Jumlah penduduk di blok tersebut | float |
| AveOccup | Rata-rata jumlah penghuni per rumah tangga | float |
| Latitude | Garis lintang lokasi blok rumah | float |
| Longitude | Garis bujur lokasi blok rumah | float |

---

## Contoh Payload (Input Valid)

```json
{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
}
```

---

## Contoh Response Sukses

```json
{
    "predicted_price": 426579.3
}
```

---

## Contoh Response Error (Input Salah Tipe)

```json
{
    "detail": [
        {
            "type": "float_parsing",
            "loc": ["body", "MedInc"],
            "msg": "Input should be a valid number, unable to parse string as a number",
            "input": "delapan"
        }
    ]
}
```

---

## Referensi

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Scikit-learn California Housing Dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
- [Repository GitHub](https://github.com/niluhmadesri/TugasKelompokPASD)


## File .joblib
- https://drive.google.com/file/d/10AnP636vFAe8ZpFHIdg7ZzxsKa6SR9IS/view?usp=sharing 
