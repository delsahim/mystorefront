from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import logging
import requests

logger = logging.getLogger(__name__)

def say_hello(request):
    try:
        logger.info('calling httpbin')
        response = requests.get('https://httpbin.org/delay/2') 
        # notify_customers.delay('Hello')
        logger.info('response received')
        data = response.json()
    except requests.ConnectionError:
        logger.critical('httpbin is offline')
    return render(request, 'hello.html', {'name': 'Mosh'})
