from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=500,verbose_name='Заголовок')
    create = models.DateTimeField(default=timezone.now,verbose_name='Дата')

    class Meta:
        ordering = ['-create']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=500,verbose_name='Заголовок')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    tags = models.ManyToManyField('Tag',blank=True,verbose_name='Теги')
    text = models.TextField(verbose_name='Содержание')
    url = models.CharField(max_length=200,verbose_name="Адрес")
    created_date = models.DateTimeField(
            default=timezone.now,verbose_name='Дата создания')
    published_date = models.DateTimeField(
            blank=True, null=True,verbose_name='Дата публикации')

    class Meta:
    	ordering = ['-created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
    	return self.title


