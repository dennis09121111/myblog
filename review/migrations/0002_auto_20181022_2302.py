# Generated by Django 2.1.1 on 2018-10-22 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]