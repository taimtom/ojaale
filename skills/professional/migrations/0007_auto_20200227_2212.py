# Generated by Django 2.2.6 on 2020-02-27 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0006_testimony_top_ten'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimony',
            old_name='top_ten',
            new_name='selected',
        ),
    ]
