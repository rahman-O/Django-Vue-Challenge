# Generated by Django 4.1.2 on 2022-10-27 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article_article_ex_article_article_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_EX',
            field=models.DateField(default=datetime.datetime(2022, 10, 27, 20, 54, 13, 26885)),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 27, 20, 54, 13, 26885)),
        ),
    ]
