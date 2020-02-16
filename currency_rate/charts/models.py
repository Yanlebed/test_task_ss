from django.db import models


class Rate(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=4)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return str(self.date)