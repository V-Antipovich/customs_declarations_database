# Generated by Django 4.1 on 2022-08-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_remove_reguser_is_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='done_registration',
            field=models.BooleanField(default=False, verbose_name='Завершил регистрацию?'),
        ),
    ]