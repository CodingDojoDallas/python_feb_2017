from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.course_name + " " + self.description
