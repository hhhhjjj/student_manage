from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=32)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.student_name


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    # when come NOT NULL constraint failed error,you should check view whether have error
    # then delete migration folder and django_migrations in databases
    course_student = models.ManyToManyField("Student")
    # one teacher to many course

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.course_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    # don't use same name as other class __str__

    class Meta:
        db_table = 'teacher'

    def __str__(self):
        return self.teacher_name

