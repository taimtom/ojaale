# Generated by Django 2.2.6 on 2020-02-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0003_professional_area_of_concentration'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='top_ten',
            field=models.BooleanField(default=False),
        ),
    ]