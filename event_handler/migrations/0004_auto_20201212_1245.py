# Generated by Django 3.1.2 on 2020-12-12 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_handler', '0003_auto_20201212_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='event_reg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event_handler.event'),
        ),
    ]
