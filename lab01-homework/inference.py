from pathlib import Path

import joblib
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegressionCV

MODEL_DIRECTORY = Path(__file__).resolve().parent / "models"

SENTIMENT_LABELS = {
    0: "negative",
    1: "neutral",
    2: "positive",
}


class SentimentAnalyzer:
    def __init__(self, model_directory: Path = MODEL_DIRECTORY) -> None:
        self.sentence_transformer = SentenceTransformer(
            str(model_directory / "sentence_transformer.model"),
            device="cpu",
            local_files_only=True,
        )
        self.classifier: LogisticRegressionCV = joblib.load(
            model_directory / "classifier.joblib"
        )

    def predict(self, text: str) -> str:
        embeddings = self.sentence_transformer.encode(
            [text],
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        predicted_class = int(self.classifier.predict(embeddings)[0])
        return SENTIMENT_LABELS[predicted_class]
