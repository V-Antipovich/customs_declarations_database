# Generated by Django 4.1 on 2022-08-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_gtdmain_currency_alter_gtdmain_currency_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtdmain',
            name='gtdId',
            field=models.CharField(max_length=23, verbose_name='Номер гтд'),
        ),
    ]