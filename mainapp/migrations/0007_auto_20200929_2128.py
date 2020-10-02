# Generated by Django 3.0.3 on 2020-09-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_products_product_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='picture',
            field=models.ImageField(upload_to='category_pictures'),
        ),
        migrations.AlterField(
            model_name='products',
            name='products_description',
            field=models.TextField(max_length=80),
        ),
    ]