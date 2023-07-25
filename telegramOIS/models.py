from django.db import models

# Create your models here.
from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.PositiveIntegerField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def check_credentials(self, username, password):
        return self.username == username and self.password == password
