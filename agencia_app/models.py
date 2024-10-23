from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    text_new = models.TextField()
    cod = models.CharField(max_length=10)


def __str__(self) -> str:
    return f'{self.title} {self.cod}'


class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
    ordering = ['id']

    

