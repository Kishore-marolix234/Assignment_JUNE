# Generated by Django 4.2.6 on 2023-11-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='canCreateAuthor',
            field=models.BooleanField(default=False),
        ),
    ]
