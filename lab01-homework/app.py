from fastapi import FastAPI

from schemas import PredictRequest, PredictResponse

app = FastAPI()


@app.post("/predict")
def predict_sentiment(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction="positive")
