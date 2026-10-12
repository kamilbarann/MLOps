import joblib
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sklearn.linear_model import LogisticRegressionCV

from app import app, sentiment_analyzer
from inference import MODEL_DIRECTORY
from schemas import PredictRequest, PredictResponse

client = TestClient(app)

SAMPLE_TEXTS = (
    "What a great MLOps lecture, I am very satisfied",
    "This movie was terrible. I hated it.",
    "The meeting starts at ten o'clock.",
)

VALID_PREDICTIONS = {"negative", "neutral", "positive"}


def test_classifier_loads_from_provided_file() -> None:
    classifier = joblib.load(MODEL_DIRECTORY / "classifier.joblib")

    assert isinstance(classifier, LogisticRegressionCV)
    assert classifier.classes_.tolist() == [0, 1, 2]


@pytest.mark.parametrize("text", SAMPLE_TEXTS)
def test_inference_for_sample_texts(text: str) -> None:
    request = PredictRequest(text=text)
    prediction = sentiment_analyzer.predict(request.text)

    assert isinstance(prediction, str)
    assert prediction in VALID_PREDICTIONS


def test_predict_returns_valid_json() -> None:
    response = client.post("/predict", json={"text": SAMPLE_TEXTS[0]})

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")

    payload = response.json()
    assert set(payload) == {"prediction"}

    validated_response = PredictResponse.model_validate(payload)
    assert validated_response.prediction == "positive"


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"text": ""},
        {"text": "   "},
        {"text": None},
        {"text": 123},
        {"text": ["example"]},
        {"text": "example", "extra": "value"},
    ],
)
def test_invalid_input_returns_json_error(payload: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        PredictRequest.model_validate(payload)

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/json")

    payload = response.json()
    assert isinstance(payload["detail"], list)
    assert payload["detail"]

    for error in payload["detail"]:
        assert isinstance(error["msg"], str)
        assert error["msg"]


@pytest.mark.parametrize("prediction", [None, 123, ["positive"]])
def test_response_rejects_non_string_prediction(prediction: object) -> None:
    with pytest.raises(ValidationError):
        PredictResponse.model_validate({"prediction": prediction})


def test_predict_uses_sentiment_model(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_predict(text: str) -> str:
        assert text == "Example text."
        return "negative"

    monkeypatch.setattr(sentiment_analyzer, "predict", fake_predict)

    response = client.post("/predict", json={"text": "Example text."})

    assert response.status_code == 200
    assert response.json() == {"prediction": "negative"}
