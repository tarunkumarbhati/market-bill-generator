# Generated by Django 2.2 on 2020-06-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountrule',
            name='discounted_item_limit_percent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
