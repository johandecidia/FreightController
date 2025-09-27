from celery.result import AsyncResult
from django.shortcuts import render
from django.http import JsonResponse
from .tasks import add_numbers


def add(request):
    body = dict(request.GET.items())
    task = add_numbers.delay(*body.values())
    return JsonResponse(task.id, safe=False)

def get_task(request, id):
    task = AsyncResult(id)
    response = dict(status=task.state, info=task.info)
    if task.successful(): response['result'] = task.result
    return JsonResponse(response, safe=False)