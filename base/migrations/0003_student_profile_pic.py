# Generated by Django 4.0.6 on 2022-08-02 14:01

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_educator_educator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=base.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]
