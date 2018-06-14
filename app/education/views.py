from django.http import HttpResponse
from django.shortcuts import render

from education.models import School, Student


def school_list(request):
    school = School.objects.all()

    return HttpResponse(school)

def student_list(request):
    student = Student.objects.all()

    return HttpResponse(student)
