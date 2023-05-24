from django.contrib.auth.models import User
from django.db import models


class BaseManager(models.Manager): pass


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Post(BaseModel):
    title = models.CharField(max_length=50, help_text='this is the title of the post', )
    body = models.TextField()
    categories = models.ForeignKey(Category, models.CASCADE, help_text='please select a category')
    author = models.ForeignKey(User, models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.id} - {self.title}'


class Comment(BaseModel):
    name = models.CharField(max_length=25)
    body = models.TextField()
    posts = models.ForeignKey(Post, models.CASCADE)

    def __str__(self):
        return f'{self.posts.pk} - {self.name}'
