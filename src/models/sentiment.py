from transformers import pipeline


sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text: str):
    if not text or len(text.strip()) == 0:
        return {"error": "Please provide some text"}
    
    result = sentiment_pipeline(text[:512])[0]
    
    return {
        "text": text,
        "sentiment": result['label'],
        "confidence": round(float(result['score']), 4),
        "model": "distilbert-base-uncased-finetuned-sst-2-english"
    }