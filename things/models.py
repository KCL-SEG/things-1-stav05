from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'name'

    is_anonymous = False

    is_authenticated = True

    name = models.CharField(
        max_length = 30,
        unique = True,
        blank = False,
    )

    description = models.CharField(
        max_length = 120,
        unique = False,
        blank = True,
    )

    quantity = models.IntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(100)],
    )