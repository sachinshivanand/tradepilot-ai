from fastapi import FastAPI

app = FastAPI(
    title="TradePilot AI",
    version="0.1.0",
    description="AI-powered NSE market scanner",
)


@app.get("/")
async def root():
    return {
        "application": "TradePilot AI",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }


@app.get("/version")
async def version():
    return {
        "version": "0.1.0",
    }