from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        error1 = {}
        if len(postData['name']) < 1:
            error1["name"] = "You must enter a course name"
        return error1;

class DescManager(models.Manager):
    def basic_validator(self, postData):
        error2 = {}
        if len(postData['desc']) < 1:
            error2["desc"] = "You must enter a course description"
        return error2;

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        error3 = {}
        if len(postData['comment']) < 1:
            error3["comment"] = "You must enter a comment"
        return error3;

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()

class Desc(models.Model):
    desc = models.TextField()
    course = models.ForeignKey(Course, related_name="descs")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = DescManager()

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CommentManager()
