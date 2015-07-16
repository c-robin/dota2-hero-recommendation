from __future__ import absolute_import

from celery import shared_task

@shared_task
def logger():
    with open("hello.txt", "w") as f:
        f.write("Hello World")