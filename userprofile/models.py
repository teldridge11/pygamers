from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

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