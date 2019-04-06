"""Posts views"""

from django.http import HttpResponse
from datetime import datetime


posts = [
  {
    'name': 'Mont Blac',
    'user': 'Yesica Cortes',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/200/?image=1036',
  },
  {
    'name': 'Mont Blac',
    'user': 'Yesica Cortes',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/200/?image=1036',
  },
  {
    'name': 'Mont Blac',
    'user': 'Yesica Cortes',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/200/?image=1036',
  },
]


def list_posts(request):
  """List existing posts"""
  content = []

  for post in posts:
    content.append("""
      <p>
        <strong>{name}</strong>
        <small>{user} - <i>{timestamp}</i></small>
        <figure><img src="{picture}"></figure>
      </p>
    """.format(**post))
    
  return HttpResponse('<br>'.join(content))

