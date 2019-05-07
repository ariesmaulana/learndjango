from django.db import models

# Create your models here.
class Mangas(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.author)