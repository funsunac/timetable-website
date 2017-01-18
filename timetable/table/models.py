from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone


class Program(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Course(models.Model):
    code = models.CharField(max_length=9)
    name = models.CharField(max_length=100)
    programs = models.ManyToManyField(Program)

    def __str__(self):
        return self.code


class Master(models.Model):
    course_code = models.CharField(max_length=8)
    cl_no = models.CharField(max_length=4)
    course_name = models.CharField(max_length=100)
    cl_day = models.IntegerField()
    cl_start_time = models.TimeField()
    cl_end_time = models.TimeField()
    cl_room = models.CharField(max_length=10)
    lecturer = models.CharField(max_length=20)

    def __str__(self):
        return '{}-{}'.format(self.course_code, self.cl_no)