# Generated by Django 4.0.6 on 2022-08-02 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educator',
            old_name='educator',
            new_name='user',
        ),
    ]
