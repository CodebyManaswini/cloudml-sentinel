from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from src.models.sentiment import analyze_sentiment

app = FastAPI(title="CloudML Sentinel - Sentiment Analysis", version="1.0.0")

# Serve static files
app.mount("/static", StaticFiles(directory="src/app/static"), name="static")

class SentimentRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(request: SentimentRequest):
    try:
        result = analyze_sentiment(request.text)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def home():
    return RedirectResponse(url="/static/index.html")

@app.get("/health")
async def health():
    return {"status": "healthy"}