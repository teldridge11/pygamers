from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.other import NullFormatter

lexer = get_lexer_by_name("python", stripall=True)
code = 'print "Hello World"'
print highlight(code, lexer, NullFormatter())

class Game(models.Model):
    user = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=256)
    image = models.ImageField(blank=True, upload_to='games')
    description = models.CharField(max_length=256)
    requirements = models.CharField(max_length=256)
    code = models.TextField()
    deleteGame = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title