# Generated by Django 2.1.4 on 2019-01-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0007_auto_20190105_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='score',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
