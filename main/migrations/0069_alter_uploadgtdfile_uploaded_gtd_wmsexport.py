# Generated by Django 4.1 on 2022-10-24 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_gtdmain_exported_to_erp_gtdmain_exported_to_wms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadgtdfile',
            name='uploaded_gtd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.uploadgtd', verbose_name='id партии загруженных ГТД'),
        ),
        migrations.CreateModel(
            name='WmsExport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('filename', models.CharField(max_length=255, verbose_name='Имя файла')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gtd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.gtdmain', verbose_name='id ГТД')),
            ],
        ),
    ]
