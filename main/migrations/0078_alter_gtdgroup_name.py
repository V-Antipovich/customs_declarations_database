# Generated by Django 4.1 on 2022-10-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0077_remove_gtdgroup_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtdgroup',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Название'),
        ),
    ]
