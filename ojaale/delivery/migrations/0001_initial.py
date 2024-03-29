# Generated by Django 2.2.6 on 2020-02-01 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('paid', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
