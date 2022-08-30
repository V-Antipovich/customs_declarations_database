# Generated by Django 4.1 on 2022-08-30 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_alter_good_marking'),
    ]

    operations = [
        migrations.AddField(
            model_name='gtdmain',
            name='last_edited',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, последний внесший изменения'),
        ),
        migrations.AddField(
            model_name='uploadgtd',
            name='who_uploaded',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, загрузивший файл(ы)'),
        ),
    ]