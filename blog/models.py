from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    author_of_publication = models.CharField(max_length=100, default="")
    publishing_house = models.CharField(max_length=100, default="")
    date_of_publication = models.CharField(max_length=100, default="")
    ISSN = models.CharField(max_length=100, default="")
    DOE = models.CharField(max_length=100, default="")
    content = models.TextField(max_length=100, default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})