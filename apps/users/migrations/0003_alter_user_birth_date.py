# Generated by Django 4.2.7 on 2023-11-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(null=True),
        ),
    ]