from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField()
    caption = models.CharField(max_length = 500)
    tag_set = models.ManyToManyField('Tag',blank=True)
    location = models.CharField(max_length = 100)

    def __str__(self):
        return self.caption

    # def get_absolute_url(self):
    #     return reverse("()", kwargs={"pk": self.pk})
    

class Tag(models.Model):
    name = models.CharField(max_length = 50, unique = True)


    def __str__(self):
        return self.name