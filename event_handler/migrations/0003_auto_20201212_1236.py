# Generated by Django 3.1.2 on 2020-12-12 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_handler', '0002_auto_20201209_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('number_of_participant', models.PositiveIntegerField()),
                ('fylier', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.AlterField(
            model_name='publisher',
            name='user_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.AddField(
            model_name='event',
            name='enrolled_participant',
            field=models.ManyToManyField(to='event_handler.Participant', verbose_name='Participant that that have enrolled for the event '),
        ),
        migrations.AddField(
            model_name='event',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participant',
            name='event_reg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event_handler.event'),
            preserve_default=False,
        ),
    ]
