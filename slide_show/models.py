from django.db import models
from random import randint

from users.models import CustomUser


class SlideShow(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False, default='Title')
    description = models.CharField(max_length=256, default='')
    time_to_show = models.IntegerField(default=20)
    secret_number = models.IntegerField(blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['secret_number', 'user'])
        ]
        unique_together = ('secret_number', 'user')

    def __str__(self):
        return f'{self.title} Slide show number: {self.secret_number}.'

    def set_new_title(self, new_title):
        self.title = new_title

    def clone_slide_show(self):
        self.pk = None
        self.secret_number = randint(1, 9999)
        self.save()
        return self.secret_number

    def share(self):
        return self.secret_number
