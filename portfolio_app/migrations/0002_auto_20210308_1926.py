# Generated by Django 3.1.7 on 2021-03-08 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='end',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='end',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='start',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start',
        ),
    ]
