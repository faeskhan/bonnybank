# Generated by Django 4.0.5 on 2022-08-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnybank_app', '0014_alter_review_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotions',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='promotions',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]