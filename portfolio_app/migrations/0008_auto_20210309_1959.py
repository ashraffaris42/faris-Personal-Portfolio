# Generated by Django 3.1.7 on 2021-03-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='backend',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='frontend',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
