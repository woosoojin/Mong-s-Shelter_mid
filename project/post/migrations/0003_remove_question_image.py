# Generated by Django 2.1.1 on 2019-07-19 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]
