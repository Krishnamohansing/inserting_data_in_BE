# Generated by Django 5.0.3 on 2024-04-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='abc123@gmail.com', max_length=254),
        ),
    ]
