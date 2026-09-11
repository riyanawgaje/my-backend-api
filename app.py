# ============================================================
# STUDENT MANAGEMENT SYSTEM
# OOP + GRADIO
# Beginner Project
# ============================================================

import gradio as gr
import os


# ============================================================
# 1. STUDENT CLASS
# ============================================================
# This class represents one student.
#
# Each student has:
# - Student ID
# - Name
# - Age
# - Course
# - Email

class Student:

    def __init__(self, student_id, name, age, course, email):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    # --------------------------------------------------------
    # Update student details
    # --------------------------------------------------------

    def update(self, name, age, course, email):

        self.name = name
        self.age = age
        self.course = course
        self.email = email

        return (
            "Student updated successfully!\n\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Course: {self.course}\n"
            f"Email: {self.email}"
        )

    # --------------------------------------------------------
    # Display student details
    # --------------------------------------------------------

    def display(self):

        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Course: {self.course}\n"
            f"Email: {self.email}"
        )


# ============================================================
# 2. STUDENT DATABASE
# ============================================================
# Dictionary is used as a simple database.
#
# Key   = Student ID
# Value = Student object

students = {}


# ============================================================
# 3. CREATE STUDENT
# ============================================================
# This function adds a new student.

def create_student(student_id, name, age, course, email):

    # Check whether Student ID is entered
    if student_id is None:

        return "Please enter Student ID."

    # Convert Student ID to integer
    try:

        student_id = int(student_id)

    except:

        return "Student ID must be a number."

    # Check whether ID already exists
    if student_id in students:

        return "Student ID already exists."

    # Check name
    if not name or name.strip() == "":

        return "Please enter student name."

    # Check age
    try:

        age = int(age)

    except:

        return "Age must be a number."

    if age <= 0:

        return "Age must be greater than 0."

    # Check course
    if not course or course.strip() == "":

        return "Please enter course."

    # Check email
    if not email or email.strip() == "":

        return "Please enter email."

    # Create Student object
    student = Student(
        student_id,
        name,
        age,
        course,
        email
    )

    # Store student
    students[student_id] = student

    return (
        "Student created successfully!\n\n"
        f"Student ID: {student_id}\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Course: {course}\n"
        f"Email: {email}"
    )


# ============================================================
# 4. UPDATE STUDENT
# ============================================================
# This function updates an existing student.

def update_student(student_id, name, age, course, email):

    if student_id is None:

        return "Please enter Student ID."

    # Convert ID to integer
    try:

        student_id = int(student_id)

    except:

        return "Student ID must be a number."

    # Check whether student exists
    if student_id not in students:

        return "Student ID not found."

    # Validate name
    if not name or name.strip() == "":

        return "Please enter student name."

    # Validate age
    try:

        age = int(age)

    except:

        return "Age must be a number."

    if age <= 0:

        return "Age must be greater than 0."

    # Validate course
    if not course or course.strip() == "":

        return "Please enter course."

    # Validate email
    if not email or email.strip() == "":

        return "Please enter email."

    # Get student object
    student = students[student_id]

    # Update details
    return student.update(
        name,
        age,
        course,
        email
    )


# ============================================================
# 5. DELETE STUDENT
# ============================================================
# This function deletes a student.

def delete_student(student_id):

    if student_id is None:

        return "Please enter Student ID."

    # Convert ID to integer
    try:

        student_id = int(student_id)

    except:

        return "Student ID must be a number."

    # Check whether student exists
    if student_id not in students:

        return "Student ID not found."

    # Get student name before deleting
    student_name = students[student_id].name

    # Delete student
    del students[student_id]

    return (
        "Student deleted successfully!\n\n"
        f"Student ID: {student_id}\n"
        f"Name: {student_name}"
    )


# ============================================================
# 6. VIEW STUDENT
# ============================================================
# This function displays one student's details.

def view_student(student_id):

    if student_id is None:

        return "Please enter Student ID."

    # Convert ID to integer
    try:

        student_id = int(student_id)

    except:

        return "Student ID must be a number."

    # Check whether student exists
    if student_id not in students:

        return "Student ID not found."

    # Get student
    student = students[student_id]

    return student.display()


# ============================================================
# 7. VIEW ALL STUDENTS
# ============================================================
# This function displays all students.

def view_all_students():

    if len(students) == 0:

        return "No students found."

    result = "========== ALL STUDENTS ==========\n\n"

    for student_id, student in students.items():

        result += (
            f"Student ID: {student.student_id}\n"
            f"Name: {student.name}\n"
            f"Age: {student.age}\n"
            f"Course: {student.course}\n"
            f"Email: {student.email}\n"
            f"{'-' * 40}\n"
        )

    return result


# ============================================================
# 8. GRADIO USER INTERFACE
# ============================================================

with gr.Blocks(title="Student Management System") as app:

    # --------------------------------------------------------
    # APPLICATION TITLE
    # --------------------------------------------------------

    gr.Markdown(
        """
        # 🎓 Student Management System

        ### OOP + Gradio CRUD Project

        Manage student records using **Create, Update, Delete and View**.
        """
    )


    # ========================================================
    # STUDENT DETAILS
    # ========================================================

    gr.Markdown("## Student Details")

    student_id = gr.Number(
        label="Student ID",
        value=101,
        precision=0
    )

    student_name = gr.Textbox(
        label="Student Name",
        placeholder="Enter student name"
    )

    student_age = gr.Number(
        label="Age",
        placeholder="Enter age",
        precision=0
    )

    student_course = gr.Textbox(
        label="Course",
        placeholder="Enter course"
    )

    student_email = gr.Textbox(
        label="Email",
        placeholder="Enter email"
    )


    # ========================================================
    # CREATE SECTION
    # ========================================================

    gr.Markdown("## Create Student")

    create_button = gr.Button(
        "Create Student"
    )

    create_output = gr.Textbox(
        label="Create Result",
        lines=7
    )

    create_button.click(
        fn=create_student,
        inputs=[
            student_id,
            student_name,
            student_age,
            student_course,
            student_email
        ],
        outputs=create_output
    )


    # ========================================================
    # UPDATE SECTION
    # ========================================================

    gr.Markdown("## Update Student")

    update_button = gr.Button(
        "Update Student"
    )

    update_output = gr.Textbox(
        label="Update Result",
        lines=7
    )

    update_button.click(
        fn=update_student,
        inputs=[
            student_id,
            student_name,
            student_age,
            student_course,
            student_email
        ],
        outputs=update_output
    )


    # ========================================================
    # DELETE SECTION
    # ========================================================

    gr.Markdown("## Delete Student")

    delete_button = gr.Button(
        "Delete Student"
    )

    delete_output = gr.Textbox(
        label="Delete Result",
        lines=5
    )

    delete_button.click(
        fn=delete_student,
        inputs=[
            student_id
        ],
        outputs=delete_output
    )


    # ========================================================
    # VIEW STUDENT
    # ========================================================

    gr.Markdown("## View Student")

    view_button = gr.Button(
        "View Student"
    )

    view_output = gr.Textbox(
        label="Student Details",
        lines=7
    )

    view_button.click(
        fn=view_student,
        inputs=[
            student_id
        ],
        outputs=view_output
    )


    # ========================================================
    # VIEW ALL STUDENTS
    # ========================================================

    gr.Markdown("## All Students")

    all_students_button = gr.Button(
        "View All Students"
    )

    all_students_output = gr.Textbox(
        label="All Student Records",
        lines=15
    )

    all_students_button.click(
        fn=view_all_students,
        inputs=[],
        outputs=all_students_output
    )


# ============================================================
# 9. RUN APPLICATION
# ============================================================

port = int(os.environ.get("PORT", 7860))

app.launch(
    server_name="0.0.0.0",
    server_port=port
)