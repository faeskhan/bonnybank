# Generated by Django 4.0.5 on 2022-08-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnybank_app', '0015_promotions_end_promotions_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=models.TextField(max_length=3000),
        ),
    ]