from django.contrib import admin
from django.db import models
from.models import Article


models_list = [Article]
admin.site.register(models_list)