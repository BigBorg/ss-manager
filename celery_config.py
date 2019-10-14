from celery.schedules import crontab
from settings import CELERY_RESULT_BACKEND, BROKER_URL

CELERYBEAT_SCHEDULE={
        "every-5-minute": {
            'task': 'modules.shadow.tasks.status_ss',
            'schedule': crontab(minute='*/5'),
        }
}