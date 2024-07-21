from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import create_connection, create_student, get_students, get_student_by_id, update_student, delete_student

app = FastAPI()
driver = create_connection()

class Student(BaseModel):
    student_id: int
    name: str
    age: int
    grade: str

@app.post("/students/")
def api_create_student(student: Student):
    create_student(driver, student.student_id, student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/students/")
def api_get_students():
    students = get_students(driver)
    return students

@app.get("/students/{student_id}")
def api_get_student(student_id: int):
    student = get_student_by_id(driver, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}")
def api_update_student(student_id: int, student: Student):
    update_student(driver, student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def api_delete_student(student_id: int):
    delete_student(driver, student_id)
    return {"message": "Student deleted successfully"}
