# Generated by Django 3.0.5 on 2020-04-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['nom']},
        ),
        migrations.AlterField(
            model_name='patient',
            name='adresse',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
