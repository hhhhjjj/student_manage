from django.shortcuts import render, redirect
from student_system.models import *


# Create your views here.
# don't use Chinese to annotation
def home(request):
    return render(request, 'home.html')


# teacher operation
def get_teacher(request):
    course_obj = {}
    teacher_list = Teacher.objects.all()
    for the_teacher in teacher_list:
        course_obj[the_teacher] = Course.objects.filter(course_teacher__teacher_name=the_teacher).all()
    return render(request, 'get_teacher.html', {"course_obj": course_obj})


def add_teacher(request):
    if request.method == "GET":
        return render(request, 'add_teacher.html')
    elif request.method == 'POST':
        add_teacher_name = request.POST.get('add_teacher_name')
        Teacher.objects.create(teacher_name=add_teacher_name)
        return redirect('/get_teacher.html')


def delete_teacher(request):
    delete_teacher_name = request.GET.get('nid')
    Teacher.objects.filter(teacher_name=delete_teacher_name).delete()
    return redirect('/get_teacher.html')


def edit_teacher(request):
    if request.method == 'GET':
        edit_teacher_name = request.GET.get('nid', '')
        obj = Teacher.objects.get(teacher_name=edit_teacher_name)
        return render(request, 'edit_teacher.html', {"obj": obj})
    elif request.method == 'POST':
        teacher_name = request.GET.get('teacher_name', '')
        edit_teacher_name = request.POST.get('edit_teacher_name', '')
        Teacher.objects.filter(teacher_name=teacher_name).update(teacher_name=edit_teacher_name)
        return redirect('/get_teacher.html')


# course operation
def get_courses(request):
    course_list = Course.objects.all()
    return render(request, 'get_courses.html', {'course_list': course_list})


def add_courses(request):
    if request.method == "GET":
        teacher_name = request.GET.get('nid', '')
        obj = Teacher.objects.get(teacher_name=teacher_name)
        return render(request, 'add_courses.html', {"obj": obj})
    elif request.method == 'POST':
        add_course_name = request.POST.get('add_course_name', '')
        # if could get error ,add "" to replace error value
        add_course_teacher = request.GET.get("nid", "")
        print(add_course_teacher)
        print(add_course_name)
        course_teacher = Teacher.objects.get(teacher_name=add_course_teacher)
        Course.objects.create(course_name=add_course_name, course_teacher=course_teacher)
        return redirect('/get_courses.html')


def delete_courses(request):
    delete_course_name = request.GET.get('nid')
    Course.objects.filter(course_name=delete_course_name).delete()
    return redirect('/get_courses.html')


def edit_courses(request):
    if request.method == 'GET':
        course_name = request.GET.get('nid', '')
        obj = Course.objects.get(course_name=course_name)
        return render(request, 'edit_courses.html', {"obj": obj})
    elif request.method == 'POST':
        course_name = request.GET.get('course_name', '')
        edit_course_name = request.POST.get('edit_course_name', '')
        Course.objects.filter(course_name=course_name).update(course_name=edit_course_name)
        return redirect('/get_courses.html')


# student operation
def get_student(request):
    student_list = Student.objects.all()
    return render(request, 'get_student.html', {'student_list': student_list})


def add_student(request):
    if request.method == "GET":
        return render(request, 'add_student.html')
    elif request.method == 'POST':
        add_student_name = request.POST.get('add_student_name')
        Student.objects.create(student_name=add_student_name)
        return redirect('/get_student.html')


def delete_student(request):
    delete_student_name = request.GET.get('nid')
    Student.objects.filter(student_name=delete_student_name).delete()
    return redirect('/get_student.html')


def edit_student(request):
    if request.method == 'GET':
        edit_student_name = request.GET.get('nid', '')
        obj = Student.objects.get(student_name=edit_student_name)
        print(obj)
        return render(request, 'edit_student.html', {"obj": obj})
    elif request.method == 'POST':
        student_name = request.GET.get('student_name', '')
        print(student_name)
        edit_student_name = request.POST.get('edit_student_name', '')
        print(edit_student_name)
        Student.objects.filter(student_name=student_name).update(student_name=edit_student_name)
        return redirect('/get_student.html')


def set_student(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        course_obj = Course.objects.get(course_name=nid)
        course_student_list = course_obj.course_student.all()
        all_student_list = Student.objects.all()
        return render(request, 'set_student.html',
                      {'course_student_list': course_student_list, 'all_student_list': all_student_list,
                       'course_obj': course_obj})
    elif request.method == 'POST':
        nid = request.GET.get('nid', '')
        ids_str = request.POST.getlist('student_name', '')
        # obj = classes.objects.get(id=nid)
        # obj.teacher.set(ids_str)
        obj = Course.objects.filter(course_name=nid).first()
        obj.course_student.set(ids_str)
        return redirect('/get_courses.html')


