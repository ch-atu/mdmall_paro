# Generated by Django 3.2 on 2022-05-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_auto_20220520_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='computergoods',
            name='detail',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='商品详情'),
        ),
        migrations.AddField(
            model_name='computergoods',
            name='packing',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='规格与包装'),
        ),
        migrations.AddField(
            model_name='computergoods',
            name='service',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='售后服务'),
        ),
        migrations.AddField(
            model_name='mobilegoods',
            name='detail',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='商品详情'),
        ),
        migrations.AddField(
            model_name='mobilegoods',
            name='packing',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='规格与包装'),
        ),
        migrations.AddField(
            model_name='mobilegoods',
            name='service',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='售后服务'),
        ),
    ]