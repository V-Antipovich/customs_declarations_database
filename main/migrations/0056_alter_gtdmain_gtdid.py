# Generated by Django 4.1 on 2022-09-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_remove_reguser_done_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtdmain',
            name='gtdId',
            field=models.CharField(max_length=23, unique=True, verbose_name='Номер гтд'),
        ),
    ]