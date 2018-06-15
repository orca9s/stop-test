from django.conf.urls import url

from education.views import school_list, student_list, school_detail, student_detail

urlpatterns = [
    url(r'^school/$', school_list),
    url(r'^school/(\d)/$', school_detail),
    url(r'^student/$', student_list),
    url(r'^student/(\d)/$', student_detail),
]