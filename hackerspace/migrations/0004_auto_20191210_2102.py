# Generated by Django 3.0 on 2019-12-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0003_auto_20191210_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_featured_photo',
            field=models.ImageField(blank=True, null=True, upload_to='event_images', verbose_name='Photo'),
        ),
    ]
