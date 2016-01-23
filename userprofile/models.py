from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    user = models.ForeignKey(User, blank=True)
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='games')
    description = models.CharField(max_length=256)
    requirements = models.CharField(max_length=256)
    code = models.CharField(max_length=256000)
    deleteGame = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

#User.game = property(lambda u: Game.objects.get_or_create(user=u)[0])