# Generated by Django 4.0.5 on 2022-07-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnybank_app', '0004_alter_event_id_alter_roomimages_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='room',
            field=models.CharField(blank=True, choices=[('night owl', 'Night Owl'), ('escarpment', 'Escarpment'), ('red squirrel', 'Red Squirrel')], max_length=12, null=True),
        ),
    ]
