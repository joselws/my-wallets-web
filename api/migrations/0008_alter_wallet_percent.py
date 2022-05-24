# Generated by Django 4.0.4 on 2022-05-24 02:43

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_wallet_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='percent',
            field=models.PositiveSmallIntegerField(default=0, validators=[api.validators.validate_100_max]),
        ),
    ]
