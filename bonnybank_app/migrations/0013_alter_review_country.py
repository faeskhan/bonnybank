# Generated by Django 4.0.5 on 2022-07-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnybank_app', '0012_alter_event_body_alter_review_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
