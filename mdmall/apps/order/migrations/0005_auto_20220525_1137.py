# Generated by Django 3.2 on 2022-05-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220524_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='specification_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='商品规格id'),
        ),
        migrations.AddField(
            model_name='ordertemp',
            name='specification_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='商品规格id'),
        ),
    ]