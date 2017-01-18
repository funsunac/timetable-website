from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Master, Program, Course
from django.shortcuts import redirect
from django import forms

dict = {'day': 'cl_day', 'code': 'course_code', 'cl_no': 'cl_no'}


def home(request):
    return redirect('/table/all')


def index(request, prog_name):
    queries = request.GET.lists()

    if prog_name == 'all':
        course_list = Master.objects.values_list('course_code', flat=True).distinct()
    else:
        course_list = [course.code for course in Course.objects.filter(programs__title=prog_name)]

    if len(queries) == 0:
        class_list = Master.objects.filter(course_code__in=course_list)
    else:
        kwargs = {}
        for key, arg in queries:
            if key == 'venue':
                kwargs[dict[key] + '__in'] = arg
            kwargs[dict[key]+'__in'] = arg
            class_list = Master.objects.filter(course_code__in=course_list).filter(**kwargs)

    class FilterForm(forms.Form):
        DAYS = (('1', 'Mon'),
                ('2', 'Tue'),
                ('3', 'Wed'),
                ('4', 'Thr'),
                ('5', 'Fri'),
                ('6', 'Sat'))
        VENUE = (('1', 'KEC'),
                 ('2', 'CIT'))
        day = forms.ChoiceField(label='', widget=forms.SelectMultiple(attrs={'id': 'dayFilter'}), choices=DAYS)

        ahh = [(course_code, Course.objects.get(code=course_code).name) for course_code in course_list]

        # Lol dafuq? I dunno how to use lamba! All hail stackoverflow! lololol
        avail_course = sorted(ahh, key=lambda tup: tup[1])
        code = forms.ChoiceField(label='', widget=forms.SelectMultiple(attrs={'id': 'courseFilter'}),
                                 choices=avail_course)

    form = FilterForm()
    form.fields['day'].initial = request.GET.getlist('day', default=[1,2,3,4,5,6])
    form.fields['code'].initial = request.GET.getlist('code', default=course_list)

    context = {'class_list': class_list,
               'filterForm': form,
               'prog_name': prog_name}

    return render(request, 'table/index.html', context)

def name(request, name):
    context = {'name': name}
    return render(request, 'table/name.html', context)