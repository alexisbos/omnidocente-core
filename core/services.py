from core.models import Student
from infra.db import get_student, save_student


def give_xp(username: str, xp: int):
    student = get_student(username)

    if not student:
        student = Student(username=username)

    student.add_xp(xp)

    save_student(student)

    return student