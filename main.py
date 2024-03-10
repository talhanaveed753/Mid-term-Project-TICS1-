import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from expense import expense_router

# Create an instance of the FastAPI class
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Define a route for the root URL ("/")
@app.get("/")
async def read_index():
    # Serve the index.html file when the root URL is accessed
    return FileResponse("./frontend/index.html")


# Include the router from expense.py to handle routes related to expenses
app.include_router(expense_router)

# Mount a static files route
# This allows the serving of static files (HTML, CSS, JavaScript, etc.) from the "frontend" directory
app.mount("/", StaticFiles(directory="frontend"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
