# Generated by Django 4.2.7 on 2023-11-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0002_alter_salons_opening_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salons',
            name='opening_time',
            field=models.CharField(max_length=5),
        ),
    ]
