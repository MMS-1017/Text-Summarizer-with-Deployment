from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import os
from textSummarizer.pipeline.prediction import PredictionPipeline

# Pydantic model for predict request:
class TextRequest(BaseModel):
    text: str

# FastAPI app initialization
app = FastAPI(title="Text Summarizer API")

# Load the PredictionPipeline once at startup
prediction_pipeline = PredictionPipeline()

# Routes
@app.get("/", tags=["Root"])
async def index():
    """Redirect to Swagger UI."""
    return RedirectResponse(url="/docs")


@app.get("/train", tags=["Training"])
async def training(background_tasks: BackgroundTasks):
    """
    Trigger model training as a background task.
    Returns immediately while training runs in background.
    """
    def run_training():
        os.system("python main.py")  # Calls your training script

    background_tasks.add_task(run_training)
    return {"message": "Training started in the background. Check logs for progress."}


@app.post("/predict", tags=["Prediction"])
async def predict_route(request: TextRequest):
    """ Generate a summary for input text. """
    try:
        summary = prediction_pipeline.predict(request.text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

# Run Uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
