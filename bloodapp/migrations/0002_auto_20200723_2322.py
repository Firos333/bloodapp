# Generated by Django 3.0.8 on 2020-07-23 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_details',
            name='Bloodbank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]