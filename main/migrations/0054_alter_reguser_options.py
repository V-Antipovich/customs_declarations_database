# Generated by Django 4.1 on 2022-09-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_alter_gtddocument_document_alter_gtddocument_group_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reguser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]