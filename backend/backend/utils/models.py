from django.db import models


class Country(models.Model):
    shortcut = models.CharField(max_length=2, primary_key=True)
    full_name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.full_name} {self.shortcut}"
