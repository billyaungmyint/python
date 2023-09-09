from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return {"message": "Hello World"}

@student_router.get('/students')
async def find_all_student():
    return listOfStudentEntity(connection.local.student.find())

@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

@student_router.put('/students/{studentId}')
async def update_student(studentId , student: Student):
    connection.local.student.find_one_and_update(
        {"_id" : ObjectId(studentId)},
        {"$set" : dict(Student)}
    )
    return studentEntity(connection.local.student.find_one({"_id" : ObjectId(studentId)}))


    
