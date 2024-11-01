# Generated by Django 5.0.7 on 2024-07-16 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measurments',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensors',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
            preserve_default=False,
        ),
    ]
