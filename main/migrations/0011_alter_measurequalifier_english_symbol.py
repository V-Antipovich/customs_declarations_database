# Generated by Django 4.1 on 2022-08-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_measurequalifier_english_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurequalifier',
            name='english_symbol',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Международное условное обозначение'),
        ),
    ]