# Generated by Django 4.2.16 on 2024-11-06 19:12

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_schedule_estimated_pickup_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='arrival',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='due',
            field=models.DateTimeField(default=dashboard.models.default_due_time),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='estimated_pickup_time',
            field=models.DateTimeField(default=dashboard.models.default_pick_time),
        ),
    ]
