# Generated by Django 4.1.4 on 2022-12-22 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_rename_activities_activity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='accessories',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='bottoms',
        ),
        migrations.RemoveField(
            model_name='category',
            name='shoes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tops',
        ),
    ]