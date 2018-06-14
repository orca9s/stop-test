from django.conf.urls import url

from education.views import school_list, student_list

urlpatterns = [
    url(r'school/', school_list),
    url(r'student/', student_list)
]