# Generated by Django 4.0.5 on 2022-07-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnybank_app', '0006_event_location_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]