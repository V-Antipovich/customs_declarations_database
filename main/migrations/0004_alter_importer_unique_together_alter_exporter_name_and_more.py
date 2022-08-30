# Generated by Django 4.1 on 2022-08-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_gtdmain_gtdid_alter_exporter_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='importer',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='exporter',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='inn',
            field=models.CharField(max_length=15, unique=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='importer',
            name='ogrn',
            field=models.CharField(max_length=20, unique=True, verbose_name='ОГРН'),
        ),
    ]