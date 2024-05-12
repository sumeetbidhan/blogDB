from fastapi import FastAPI
from routes.healthCheck import entry_root
from routes.blogService import blog_root


app = FastAPI()


app.include_router(entry_root)
app.include_router(blog_root)