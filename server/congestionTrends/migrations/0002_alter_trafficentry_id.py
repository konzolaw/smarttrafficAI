# Generated by Django 5.2 on 2025-04-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congestionTrends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficentry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
