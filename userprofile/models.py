from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=56)
    image = models.ImageField(upload_to='games')
    description = models.TextField()
    requirements = models.TextField()
    code = models.TextField()

    def __unicode__(self):
        return self.title

#User.game = property(lambda u: Game.objects.get_or_create(user=u)[0])