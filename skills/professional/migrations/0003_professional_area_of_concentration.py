# Generated by Django 2.2.6 on 2020-02-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0002_auto_20200222_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='area_of_concentration',
            field=models.TextField(blank=True, help_text='seperate each with comma (,)', null=True),
        ),
    ]