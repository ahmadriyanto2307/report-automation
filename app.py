from fastapi import FastAPI

app = FastAPI(
    title="Report Automation API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "OK",
        "project": "Report Automation"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }