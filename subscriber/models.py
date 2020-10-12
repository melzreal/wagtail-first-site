from django.db import models

class Subscriber(models.Model):
    email = models.CharField(max_length = 100, blank=False, null=False, help_text="email address")
    full_name = models.CharField(max_length = 100, blank=False, null=False, help_text="full name")

    def __str__(self):
        return self.full_name