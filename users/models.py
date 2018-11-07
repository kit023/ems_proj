from django.db import models

from django.contrib.auth.models import AbstractUSer

class Participant(AbstractUser):
    contact_nujmber = models.CharField("Contact Number", max_length = 50)

    def __str__(self)
        return self.username
