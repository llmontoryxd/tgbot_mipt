from django.db import models


class Words(models.Model):

    word = models.CharField(verbose_name='Word', max_length=100)
    translation = models.CharField(verbose_name='Translation', max_length=100)

    def __str__(self):
        return self.word + ' ' + self.translation

