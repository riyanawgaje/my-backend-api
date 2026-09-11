"""
CODE 1

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
      return {"message" : "Hello FastAPI"}
"""

"""
CODE 2

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
      return {"message" : "Hello GAYATRI"}
"""
"""
CODE 3
#To run code after url add/docs

from fastapi import FastAPI

app = FastAPI()
@app.get("/students/{student_id}")
def get_student(student_id: int):   
    return {"student_id": student_id}
# /students/101

"""

"""
CODE 4


from fastapi import FastAPI

app = FastAPI()
@app.get("/students")
def get_students(name: str):
    return {"name": name}
# /students?name=Rahul
"""

"""
CODE 5

from unicodedata import name

from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()


# CREATE student
# This endpoint accepts student information
@app.post("/students")
def create_student(name: str, course: str, marks: int):

# Create a student dictionary
    student = {
"name": name,
"course": course,
"marks": marks
}

# Return the data received from the client0
    return {
"message": "Student created successfully",
"student": student
}
"""

""" 

 CODE 6
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()


# Temporary student data
students = [
{
"id": 1,
"name": "Ram",
"course": "Python",
"marks": 85
},
{
"id": 2,
"name": "diya",
"course": "AI",
"marks": 90
}
]


#GET END points
@app.get("/students")
def get_students():

# Return all students
    return students

"""

"""

CODE 7


from unicodedata import name

from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()


# CREATE student
# This endpoint accepts student information
@app.post("/students")
def create_student(name: str, course: str, marks: int):

# Create a student dictionary
    student = {
"name": name,
"course": course,
"marks": marks
}

# Return the data received from the client
    return {
"message": "Student created successfully",
"student": student
}

# READ ALL students
# This endpoint returns all student information
@app.get("/students")
def read_all_students():

    # Create a list of students
    students = [
        {
            "id": 1,
            "name": "Ram",
            "course": "Python",
            "marks": 85
        },
        {
            "id": 2,
            "name": "Diya",
            "course": "AI",
            "marks": 90
        }
    ]

    # Return all students
    return students

# READ ONE student
# This endpoint returns information of one student
@app.get("/students/{student_id}")
def read_one_student(student_id: int):

    # Create a student list
    students = [
        {
            "id": 1,
            "name": "Ram",
            "course": "Python",
            "marks": 85
        },
        {
            "id": 2,
            "name": "Diya",
            "course": "AI",
            "marks": 90
        }
    ]

    # Search for the student
    for student in students:
        if student["id"] == student_id:
            return student

    # If student is not found
    return {"message": "Student not found"}

# UPDATE student
# This endpoint updates student information
@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, course: str, marks: int):

    # Create a student list
    students = [
        {
            "id": 1,
            "name": "Ram",
            "course": "Python",
            "marks": 85
        },
        {
            "id": 2,
            "name": "Diya",
            "course": "AI",
            "marks": 90
        }
    ]

    # Search for the student
    for student in students:
        if student["id"] == student_id:

            # Update student information
            student["name"] = name
            student["course"] = course
            student["marks"] = marks

            # Return updated student
            return {
                "message": "Student updated successfully",
                "student": student
            }

    # If student is not found
    return {"message": "Student not found"}


    # DELETE student
# This endpoint deletes a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    # Create a student list
    students = [
        {
            "id": 1,
            "name": "Ram",
            "course": "Python",
            "marks": 85
        },
        {
            "id": 2,
            "name": "Diya",
            "course": "AI",
            "marks": 90
        }
    ]

    # Search for the student
    for student in students:
        if student["id"] == student_id:

            # Remove the student
            students.remove(student)

            # Return success message
            return {
                "message": "Student deleted successfully",
                "student": student
            }

    # If student is not found
    return {"message": "Student not found"}

"""

"""
CODE 8
"""

from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Create FastAPI application
app = FastAPI()

# Get Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect Python to Supabase
supabase = create_client(
SUPABASE_URL,
SUPABASE_KEY
)
#The important part is:
supabase = create_client(
SUPABASE_URL,
SUPABASE_KEY,
)

print("Connected the supabase successfully!!")
@app.post("/students")   # it will create the POST endpoint
def create_student(name: str, course: str, marks: int):

# Data to be inserted into Supabase
    student = {
        "name": name,
        "course": course,
        "marks": marks
    }

# Insert student into Supabase
    response = (
        supabase
        .table("student")
        .insert(student)
        .execute()
    )

# Return database response
    return {
        "message": "Student created successfully",
        "data": response.data
    }

# GET method - Get all students 
@app.get("/students") 
def get_students(): 
    # Get students from Supabase 
    response = ( 
        supabase 
        .table("student") 
        .select("*") 
        .execute() 
    ) 

    # Return database response 
    return { 
        "message": "Students retrieved successfully", 
        "data": response.data 
    }
# UPDATE method - Update a student 
@app.put("/students/{student_id}") 
def update_student( 
    student_id: int, 
    name: str, 
    course: str, 
    marks: int 
): 
    # Data to update 
    student = { 
        "name": name, 
        "course": course, 
        "marks": marks 
    } 

    # Update student in Supabase 
    response = ( supabase 
                .table("student") 
                .update(student) 
                .eq("id", student_id) 
                .execute() 
    ) 

    # Return database response 
    return { 
        "message": "Student updated successfully", 
        "data": response.data 
    } 

# DELETE method - Delete a student 
@app.delete("/students/{student_id}") 
def delete_student(student_id: int): 

    # Delete student from Supabase 
    response = ( 
        supabase 
        .table("student") 
        .delete() 
        .eq("id", student_id) 
        .execute() 
    ) 

    # Return database response 
    return { 
        "message": "Student deleted successfully", 
        "data": response.data 
    }