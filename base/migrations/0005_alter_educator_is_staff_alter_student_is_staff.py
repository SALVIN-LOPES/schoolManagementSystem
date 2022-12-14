# Generated by Django 4.0.6 on 2022-08-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_educator_is_staff_student_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educator',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='educator'),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='educator'),
        ),
    ]
