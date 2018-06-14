from django.http import HttpResponse
from django.shortcuts import render

from education.models import School, Student


def school_list(request):
    schools = School.objects.all()

    context = {
        'schools': schools,
    }

    return render(request, 'school_list.html', context)


def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, context)
