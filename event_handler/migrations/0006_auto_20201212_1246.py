# Generated by Django 3.1.2 on 2020-12-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_handler', '0005_auto_20201212_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='enrolled_participant',
            field=models.ManyToManyField(blank=True, to='event_handler.Participant', verbose_name='Participant that that have enrolled for the event '),
        ),
    ]
