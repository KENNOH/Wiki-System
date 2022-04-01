from celery import Celery
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User
from wiki_system.celery import app
from django.utils import timezone
from celery import shared_task
import datetime
from datetime import timedelta
from celery.schedules import crontab
from django.db import transaction
from .models import *
from django.conf import settings



@app.task(bind=True, reject_on_worker_lost=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True, retry_kwargs={'max_retries': 5})
def update_wiki_views(self,data):
    try:
        unique_id = data.get('unique_id')
        with transaction.atomic():
            subscription = WikiSearch.objects.select_for_update().get(unique_id=unique_id)
            subscription.views+=1
            subscription.save()
    except:
        self.retry()