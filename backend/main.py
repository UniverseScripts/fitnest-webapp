from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.database import init_db
from routers import auth, listings, matches, chat, test, onboarding


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting Fitness API...")
    try:
        await init_db()
        print("✅ Database connected & Tables have been created.")
    except Exception as e:
        print(f"❌ Failed to connect to the database: {e}")
    yield
    print("🛑 Shutting down Fitness API")

app = FastAPI(title="Fitnest", description="A web application dedicated to room and friend matching.",
              version="1.0.0", lifespan=lifespan)

origins = ["http://localhost:3000", "http://localhost:5173", "http://localhost:8000/chat/conversations"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Include all routers
app.include_router(auth.router)
app.include_router(listings.router)
app.include_router(matches.router)
app.include_router(chat.router)
app.include_router(test.router)
app.include_router(onboarding.router)

@app.get("/")
async def health_check():
    return {"status": "active", "project": "Fitnest"}
