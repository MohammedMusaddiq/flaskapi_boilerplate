from resources.extensions import celery


@celery.task(name="add")
def add(x, y):
    return x + y
