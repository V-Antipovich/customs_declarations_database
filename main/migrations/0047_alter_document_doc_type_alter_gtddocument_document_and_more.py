# Generated by Django 4.1 on 2022-08-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_alter_gtdmain_currency_alter_gtdmain_customs_house_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.documenttype', verbose_name='Id типа документа'),
        ),
        migrations.AlterField(
            model_name='gtddocument',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.document', verbose_name='id документа'),
        ),
        migrations.AlterField(
            model_name='gtdgroup',
            name='tn_ved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.tnved', verbose_name='id кода товарной группы ТН ВЭД'),
        ),
    ]