from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.topic_name  # To display topic name in admin
