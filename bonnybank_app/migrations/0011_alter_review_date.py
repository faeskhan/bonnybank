# Generated by Django 4.0.5 on 2022-07-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnybank_app', '0010_remove_roomimages_room_delete_room_delete_roomimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
