# Generated by Django 2.2.6 on 2020-02-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
