from pathlib import Path

import joblib
from sklearn.linear_model import LogisticRegression

MODEL_PATH = Path(__file__).resolve().parent / "iris_model.joblib"


def load_model() -> LogisticRegression:
    return joblib.load(MODEL_PATH)


def predict(
    model: LogisticRegression,
    features: dict[str, float],
) -> str:
    sample = [
        [
            features["sepal_length"],
            features["sepal_width"],
            features["petal_length"],
            features["petal_width"],
        ]
    ]

    predicted_class = model.predict(sample)[0]
    return str(predicted_class)
