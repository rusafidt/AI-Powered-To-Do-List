from logging import Logger
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import spacy
import os

# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered To-Do List API",
    description="An intelligent to-do list API that automatically categorizes tasks using NLP",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy's small English model (includes tokenizer, POS tagger, lemmatizer, etc.)
def load_spacy_model():
    """
    Load spaCy model with safe fallbacks:
    1. Try to load en_core_web_sm (works if installed via pip/requirements.txt).
    2. Try a blank English pipeline (tokenizer only).
    """
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        Logger.info("⚠ spaCy model 'en_core_web_sm' not installed. Using blank English instead.")
        return spacy.blank("en")
    except Exception as e:
        Logger.error(f"Unexpected spaCy error: {e}")
        return None

nlp = load_spacy_model()

# Define categories and the keywords that hint at them
CATEGORIES = {
    "Shopping": ["buy", "purchase", "order", "milk", "grocery", "shop"],
    "Work": ["email", "report", "meeting", "project", "deadline"],
    "Health": ["exercise", "run", "gym", "doctor", "medicine"],
    "Personal": ["call", "visit", "family", "friend", "birthday"],
}

# Pydantic models for request/response
class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    task: str
    category: str

class BatchTaskRequest(BaseModel):
    tasks: List[str]

class BatchTaskResponse(BaseModel):
    results: List[TaskResponse]

class HealthResponse(BaseModel):
    status: str
    message: str

def auto_tag(task: str) -> str:
    if not nlp or "lemmatizer" not in nlp.pipe_names:
        # fallback: keyword-only matching
        task_lower = task.lower()
        for category, keywords in CATEGORIES.items():
            for keyword in keywords:
                if keyword in task_lower:
                    return category
        return "Other"

    doc = nlp(task.lower())
    for token in doc:
        for category, keywords in CATEGORIES.items():
            if token.lemma_ in keywords:
                return category
    return "Other"


# API Endpoints
@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint with API information"""
    return HealthResponse(
        status="success",
        message="AI-Powered To-Do List API is running! Visit /docs for API documentation."
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="API is running successfully"
    )

@app.get("/healthz")
async def healthz():
    """Render health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="API is running successfully"
    )

@app.post("/tag-task", response_model=TaskResponse)
async def tag_single_task(request: TaskRequest):
    """
    Tag a single task with an appropriate category
    """
    if not request.task.strip():
        raise HTTPException(status_code=400, detail="Task cannot be empty")
    
    category = auto_tag(request.task)
    return TaskResponse(task=request.task, category=category)

@app.post("/tag-tasks", response_model=BatchTaskResponse)
async def tag_multiple_tasks(request: BatchTaskRequest):
    """
    Tag multiple tasks with appropriate categories
    """
    if not request.tasks:
        raise HTTPException(status_code=400, detail="Tasks list cannot be empty")
    
    results = []
    for task in request.tasks:
        if not task.strip():
            continue
        category = auto_tag(task)
        results.append(TaskResponse(task=task, category=category))
    
    return BatchTaskResponse(results=results)

@app.get("/categories")
async def get_categories():
    """
    Get all available categories and their keywords
    """
    return {"categories": CATEGORIES}

# Demo endpoint for testing
@app.get("/demo")
async def demo():
    """
    Demo endpoint showing example tasks and their categories
    """
    demo_tasks = [
        "Buy milk and bread",
        "Finish project report", 
        "Go to the gym",
        "Call mom about birthday",
        "Book flight tickets"
    ]
    
    results = []
    for task in demo_tasks:
        category = auto_tag(task)
        results.append(TaskResponse(task=task, category=category))
    
    return {"demo_results": results}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
