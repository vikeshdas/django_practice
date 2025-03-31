from django.db import models

class Topic(models.Model):
    topic_name=models.CharField(max_length=256,unique=True)
    
    def __str__(self):
        return self.topic_name
    
class WebPage(models.Model):
    Topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    url=models.URLField(unique=True)

    def __str__(self):
        return str(self.date)

