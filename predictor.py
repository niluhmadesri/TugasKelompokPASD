
import joblib
import numpy as np

def load_model(path="/content/house_price_model.joblib"):
    try:
        model = joblib.load(path)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"File model tidak ditemukan di path: {path}")

def preprocess(data: dict):
    expected_features = [
        "MedInc", "HouseAge", "AveRooms", "AveBedrms",
        "Population", "AveOccup", "Latitude", "Longitude"
    ]

    missing = [f for f in expected_features if f not in data]
    if missing:
        raise ValueError(f"Fitur berikut tidak ditemukan: {missing}")

    for key in expected_features:
        if not isinstance(data[key], (int, float)):
            raise TypeError(f"Nilai '{key}' harus berupa angka, bukan {type(data[key]).__name__}")

    input_array = np.array([[data[f] for f in expected_features]])
    return input_array

def predict(data: dict):
    try:
        model = load_model()
        input_array = preprocess(data)
        result = model.predict(input_array)
        return {"predicted_price": round(float(result[0]) * 100000, 2)}
    except (ValueError, TypeError) as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Terjadi kesalahan tidak terduga: {str(e)}"}
