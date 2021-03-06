# Generated by Django 3.1.7 on 2021-03-09 16:06

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_delete_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
