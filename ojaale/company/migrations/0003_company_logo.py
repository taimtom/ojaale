# Generated by Django 2.2.6 on 2020-02-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default=1, upload_to='company/images'),
            preserve_default=False,
        ),
    ]
