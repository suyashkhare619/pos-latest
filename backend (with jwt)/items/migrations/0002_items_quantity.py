# Generated by Django 2.0.4 on 2018-05-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
