from django.db import models
from random import randint


class SlideShow(models.Model):
    title = models.CharField(max_length=50, blank=False)
    secret_number = models.IntegerField(blank=False)

#    def __init__(self,  *args, **kwargs):
#        print("ey")
#        secret_number = randint(0, 999)
#        self.secret_number = secret_number
#        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.title} Slide show number: {self.secret_number}.'
