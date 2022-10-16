# Generated by Django 3.2 on 2022-05-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': '订单支付', 'verbose_name_plural': '订单支付'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='支付的订单号'),
        ),
    ]