# Generated by Django 4.1 on 2022-08-31 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_alter_gtddocument_gtd_alter_gtdgood_gtd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtddocument',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.document', verbose_name='id документа'),
        ),
        migrations.AlterField(
            model_name='gtddocument',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.gtdgroup', verbose_name='id группы товаров'),
        ),
        migrations.AlterField(
            model_name='gtdgood',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.gtdgroup', verbose_name='id группы товаров'),
        ),
    ]
