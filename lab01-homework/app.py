from fastapi import FastAPI

from inference import SentimentAnalyzer
from schemas import PredictRequest, PredictResponse

app = FastAPI()
sentiment_analyzer = SentimentAnalyzer()


@app.post("/predict")
def predict_sentiment(request: PredictRequest) -> PredictResponse:
    prediction = sentiment_analyzer.predict(request.text)
    return PredictResponse(prediction=prediction)
