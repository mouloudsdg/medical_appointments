# Generated by Django 3.0.5 on 2020-04-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200417_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]