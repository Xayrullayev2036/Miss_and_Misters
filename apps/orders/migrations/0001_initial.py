# Generated by Django 4.2.7 on 2023-11-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_price', models.IntegerField()),
                ('order_status', models.CharField(choices=[('yangi', 'YANGI'), ('kutmoqda', 'KUTMOQDA'), ('toxtatildi', 'TOXTATILDI'), ('yakunlandi', 'YAKUNLANDI')], max_length=255)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
