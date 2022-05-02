import shlex
import sys
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery_workers():
    cmd = 'pkill -f "celery"'
    if sys.platform == 'win32':
        cmd = 'taskkill /f /t /im celery.exe'
    subprocess.call(shlex.split(cmd))
    subprocess.call(shlex.split('celery -A wiki_system worker --concurrency=3 -l info'))


def restart_celery_beat():
    cmd = 'pkill -f "beat"'
    if sys.platform == 'win32':
        cmd = 'taskkill /f /t /im celery.exe'
    subprocess.call(shlex.split(cmd))
    subprocess.call(shlex.split('celery -A wiki_system beat -l info'))



class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        autoreload.run_with_reloader(restart_celery_workers)
        print('Starting celery beat with autoreload...')
        autoreload.run_with_reloader(restart_celery_beat)

