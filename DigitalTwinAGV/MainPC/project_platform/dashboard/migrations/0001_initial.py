# Generated by Django 4.2.16 on 2024-11-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=100)),
                ('arrival', models.DateTimeField()),
                ('due', models.DateTimeField()),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('placed_at', models.DateTimeField(blank=True, null=True)),
                ('estimated_time', models.DurationField()),
                ('actual_time', models.DurationField()),
                ('delay', models.DurationField(blank=True, null=True)),
                ('on_time', models.BooleanField(default=True)),
            ],
        ),
    ]