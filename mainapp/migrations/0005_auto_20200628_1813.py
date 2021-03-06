# Generated by Django 3.0.3 on 2020-06-28 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200628_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='products_description',
            field=models.TextField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(upload_to='products_pictures'),
        ),
        migrations.CreateModel(
            name='product_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='more_product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.products')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
    ]
