# Generated by Django 2.2.6 on 2020-02-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='features',
            field=models.CharField(blank=True, help_text='separate each with comma (,)', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirement',
            field=models.TextField(blank=True, help_text='separate each by comma (,)', null=True),
        ),
    ]
