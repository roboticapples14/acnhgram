# Generated by Django 3.0.8 on 2020-07-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0010_auto_20200704_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showcasepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
