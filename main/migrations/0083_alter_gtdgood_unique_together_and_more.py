# Generated by Django 4.1 on 2022-11-04 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0082_handbook'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gtdgood',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='gtdgroup',
            unique_together=set(),
        ),
    ]
