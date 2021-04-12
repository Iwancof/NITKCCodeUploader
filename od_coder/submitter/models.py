from django.db import models
from django.utils import timezone

from enum import Enum

# Create your models here.

class Task(models.Model):
    auther = models.CharField(max_length=100)
    task_text = models.CharField(max_length=1000)
    test_cases = models.CharField(max_length=10000)
    limit = models.DateField('Submit limit', default=timezone.now())
    hidden = models.BooleanField(default=False)
    test_enable = models.BooleanField(default=True)

    def __str__(self):
        return "task: {}, auther: {}, limit: {}".format(self.task_text, self.auther, str(self.limit))

class SubmitResult(Enum):
    DISABLE = 0
    NOTSUBMITTED = 1
    AC = 2
    RE = 3
    TLE = 4

class Submit(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.CharField(max_length=100)
    result = models.IntegerField(default = 0)

    def __str__(self):
        return self.student



