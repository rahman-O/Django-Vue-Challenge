from django.db import models
from datetime import datetime
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.CharField(max_length=250)
    article_created = models.DateField(default=datetime.now())
    article_EX = models.DateField(default=datetime.now())

    
