import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def sample_classroom():
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student{i}") for i in range(10)]
    return Classroom(teacher, students, "Potions")


def test_add_student(sample_classroom):
    # Test adding a student within the limit
    new_student = Student("Harry Potter")
    sample_classroom.add_student(new_student)
    assert new_student in sample_classroom.students

    # Test adding a student beyond the limit
    with pytest.raises(TooManyStudents):
        sample_classroom.add_student(Student("Draco Malfoy"))


def test_remove_student(sample_classroom):
    # Test removing an existing student
    student_to_remove = sample_classroom.students[0]
    sample_classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in sample_classroom.students

    # Test removing a non-existing student
    with pytest.raises(ValueError):
        sample_classroom.remove_student("Cedric Diggory")


def test_change_teacher(sample_classroom):
    new_teacher = Teacher("Professor McGonagall")
    sample_classroom.change_teacher(new_teacher)
    assert sample_classroom.teacher == new_teacher


@pytest.mark.parametrize("student_count", [5, 10, 15])
def test_add_student_parameterized(sample_classroom, student_count):
    new_students = [Student(f"Student{i}") for i in range(student_count)]

    # Test adding students within the limit
    sample_classroom.students = []
    for student in new_students:
        sample_classroom.add_student(student)
    assert all(student in sample_classroom.students for student in new_students)

    # Test adding students beyond the limit
    with pytest.raises(TooManyStudents):
        sample_classroom.add_student(Student("Extra Student"))
