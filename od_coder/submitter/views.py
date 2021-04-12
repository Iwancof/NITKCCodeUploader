from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models

from django.views import generic

# Create your views here.

def index(request):
    if request.user.is_authenticated == False:
        return render(request, "submitter/unauthorized.html")

    all_visiable_tasks = models.Task.objects.filter(hidden=False)
    students_submits = models.Submit.objects.filter(student=request.user.get_username)

    tasks = []
    for task in all_visiable_tasks:
        res = models.SubmitResult.NOTSUBMITTED
        if models.Task.test_enable == False:
            res = models.SubmitResult.DISABLE
        for s in students_submits.filter(task = task):
            if s.result == SubmitResult.AC:
                res = models.SubmitResult.AC;


        tasks.append(TaskWrapper(task, res))
    
    context = {
            "DISABLE": models.SubmitResult.DISABLE,
            "NOTSUBMITTED": models.SubmitResult.NOTSUBMITTED,
            "AC": models.SubmitResult.AC,
            "RE": models.SubmitResult.RE,
            "TLE": models.SubmitResult.TLE,
            }

    context['tasks'] = tasks

    return render(request, "submitter/index.html", context)

class TaskWrapper:
    def __init__(self, task, result):
        self.task = task
        self.result = result

    def __str__(self):
        return "task: {}, ret = {}".format(str(self.task), str(self.result))

def task_detail(response, task_id):
    task = models.Task.objects.get(pk = task_id)
    context = {
            'task': task
            }
    return render(response, 'submitter/task.html', context)


