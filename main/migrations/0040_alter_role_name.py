# Generated by Django 4.1 on 2022-08-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_role_users_reguser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Роль'),
        ),
    ]
