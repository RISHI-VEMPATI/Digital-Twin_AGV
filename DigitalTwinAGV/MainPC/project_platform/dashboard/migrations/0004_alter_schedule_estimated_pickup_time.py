# Generated by Django 4.2.16 on 2024-11-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='estimated_pickup_time',
            field=models.DateTimeField(),
        ),
    ]
