# Generated by Django 3.1 on 2020-10-01 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0007_yfcase_yfcasefinaldecision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yfcase',
            name='yfcaseFinalDecision',
        ),
    ]
