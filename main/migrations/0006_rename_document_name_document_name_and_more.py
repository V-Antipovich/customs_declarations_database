# Generated by Django 4.1 on 2022-08-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_exporter_unique_together_alter_exporter_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='document_name',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='gtdgroup',
            unique_together={('gtd', 'number')},
        ),
    ]