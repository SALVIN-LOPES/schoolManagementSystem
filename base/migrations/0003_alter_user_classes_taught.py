# Generated by Django 4.0.6 on 2022-08-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_classes_taught_user_grade_user_roll_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='classes_taught',
            field=models.CharField(default='null', max_length=100),
        ),
    ]