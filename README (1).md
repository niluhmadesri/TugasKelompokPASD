
# House Price Prediction API

API berbasis FastAPI untuk memprediksi harga rumah menggunakan model Random Forest yang dilatih pada dataset California Housing.

---

## Instalasi Dependencies

pip install fastapi uvicorn pyngrok scikit-learn joblib numpy

---

## Cara Menjalankan Server

uvicorn main:app --host 0.0.0.0 --port 8000

---

## Endpoint

### GET /
Mengecek apakah server berjalan.

**Response:**
{"message": "House Price Prediction API is running!"}

### POST /predict
Menerima data rumah dalam format JSON dan mengembalikan prediksi harga.

---

## Contoh Payload (Input Valid)

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

## Contoh Response Sukses

{
    "predicted_price": 426579.3
}

---

## Contoh Response Error (Input Salah Tipe)

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

---

## Deskripsi Fitur Input

| Fitur       | Deskripsi                              | Tipe  |
|-------------|----------------------------------------|-------|
| MedInc      | Median pendapatan rumah tangga          | float |
| HouseAge    | Usia rata-rata rumah                   | float |
| AveRooms    | Rata-rata jumlah ruangan               | float |
| AveBedrms   | Rata-rata jumlah kamar tidur           | float |
| Population  | Jumlah penduduk di blok tersebut       | float |
| AveOccup    | Rata-rata jumlah penghuni              | float |
| Latitude    | Garis lintang lokasi rumah             | float |
| Longitude   | Garis bujur lokasi rumah               | float |
