"""Platzigram views"""
from django.http import HttpResponse

from datetime import datetime
import json

def hello_world(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse(f'Oh, hi! Current server time is {now}')

def sort_integers(request):
  numbers = [int(item) for item in request.GET['numbers'].split(',')]
  numersOrdered = sorted(numbers)
  data = {
    'status': 'ok',
    'numbers': numersOrdered,
    'message': 'Integers sorted successfully'
  }
  return HttpResponse(
    json.dumps(data, indent=4), 
    content_type='application/json'
  )

def say_hi(request, name, age):
  """Return a greeting"""
  if age < 12:
    message = f'Sorry {name}, you are not allowed here'
  else:
    message = f'Hello, {name}! Welcome to Platzigram'
  return HttpResponse(message)
