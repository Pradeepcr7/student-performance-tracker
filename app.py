import streamlit as st
from student_logic import Student

st.title("📘 Student Performance Tracker")
name = st.text_input("Enter student name")

subjects = ["Tamil", "English", "Math", "Science", "Computer Science"]
marks = {}
for subject in subjects:
    mark = st.number_input(f"Enter marks for {subject}", min_value=0, max_value=100, step=1)
    marks[subject] = mark

if st.button("Show Result"):
    student = Student(name, marks)
    avg = student.calculate_average()
    grade = student.get_grade()
    result = student.get_results()

    st.success(f"Student Name: {student.name}")
    st.info(f"Average Marks: {avg:.2f}")
    st.warning(f"Grade: {grade}")

    if result == "Pass":
        st.success(f"🎉 Congratulations {student.name}, you passed the exam!")
    else:
        st.error(f"❌ Sorry {student.name}, you failed. Please try again.")
