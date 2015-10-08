from math import factorial

from celery import Celery
from sqlalchemy import create_engine

engine = create_engine('sqlite:///celery.db', echo=True)


app = Celery('tasks', backend='db+sqlite:///celery.db',
             broker='amqp://guest@localhost//')


@app.task
def compute_factorial(x):
    """ Compute factorial of x"""
    return factorial(x)
