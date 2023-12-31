from django.db import models

class Comment(models.Model):
    fullName = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=70, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    checked = models.BooleanField( default=False, blank=False)

    def __str__(self):
        return f'{self.fullName}/{self.checked}'