import django_filters

from .models import Attendence

class AttendenceFilter(django_filters.FilterSet):
    Student_ID = django_filters.CharFilter(label="Matriculation #")
    year = django_filters.CharFilter(label="Semester")
    period = django_filters.CharFilter(label="Lecture")

    class Meta:
        model = Attendence
        fields = '__all__'
        exclude = ['Faculty_Name', 'status','time','branch','section']