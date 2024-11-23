from fastapi import FastAPI
from .books import router as books_router
from .authors import router as authors_router

def create_app() -> FastAPI:
    app = FastAPI()
    
    # Include routers for books and authors
    app.include_router(books_router)
    app.include_router(authors_router)
    
    return app
