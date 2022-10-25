# Generated by Django 4.1 on 2022-10-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0073_remove_reguser_roles_delete_jobtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Должность')),
            ],
        ),
        migrations.AddField(
            model_name='reguser',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='+', to='main.jobtitle', verbose_name='Должность'),
        ),
    ]
