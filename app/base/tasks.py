from celery import shared_task
from time import sleep


@shared_task(name='base.add_numbers')
def add_numbers(*args) -> int:
    sleep(5)
    numbers = [int(arg) for arg in args]
    return sum(numbers)