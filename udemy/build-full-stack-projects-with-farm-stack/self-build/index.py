from fastapi import FastAPI
from routes.student import student_router

#create app object
app = FastAPI()

app.include_router(student_router)

