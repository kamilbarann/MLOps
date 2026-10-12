from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.utils import Bunch

MODEL_PATH = Path(__file__).resolve().parent / "iris_model.joblib"


def load_data() -> Bunch:
    return load_iris()


def train_model(dataset: Bunch) -> LogisticRegression:
    model = LogisticRegression(max_iter=200)
    model.fit(dataset.data, dataset.target)
    return model


def save_model(model: LogisticRegression) -> None:
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    iris_dataset = load_data()
    trained_model = train_model(iris_dataset)
    save_model(trained_model)
    print(f"Model saved to {MODEL_PATH}")
