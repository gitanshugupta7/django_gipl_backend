# Generated by Django 3.0.3 on 2020-10-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20201023_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='summary',
            field=models.TextField(default='summary', max_length=100),
        ),
    ]