# Generated by Django 5.1.6 on 2025-02-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
