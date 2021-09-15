from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.management import call_command

from django.core.mail import send_mail

import accounts.models
import quiz.models


logger = get_task_logger(__name__)

@shared_task
def sample_task():
    logger.info(">>>>> THE SAMPLE TASK JUST RUN <<<<<")
    # print('test')

@shared_task
def send_email_report():
    call_command('email_report')




