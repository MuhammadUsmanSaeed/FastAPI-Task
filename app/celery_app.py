from celery import Celery
from celery.schedules import crontab

celery = Celery('app', broker='amqp://guest:guest@rabbitmq:5672//', include=['app.celery_task'])

celery.conf.beat_schedule = {
    'add-every-tues': {
        'task': 'celery_item',
        'schedule': crontab(minute='*/1'),
        'args': (1,),
    },
}
celery.conf.timezone = 'UTC'
