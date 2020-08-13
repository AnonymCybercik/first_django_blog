import datetime
from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Maqola nomi', max_length=200)
    article_text = models.TextField('Maqola matni')
    pub_date = models.DateTimeField('Maqola vaqti')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
    
    class Meta():
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Izoh muallifi', max_length=200)
    comment_text = models.CharField('Izoh:', max_length=200)
    def __str__(self):
        return self.author_name
    
    class Meta():
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
