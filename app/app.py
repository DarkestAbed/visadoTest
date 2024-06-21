# app/api.py

import app.assets

from fastapi import FastAPI


app = FastAPI(
    debug=True,
    title="Visador Creditia",
    description="API de visado y evaluación de clientes",
    version="0.0.1",
)


@app.get("/hello")
async def root() -> dict:
    return {
        "message": "Hello World",
    }


@app.get("/public")
def public() -> dict:
    """A public endpoint that does not require any authentication."""
    return {
        "message": "Public endpoint",
    }
