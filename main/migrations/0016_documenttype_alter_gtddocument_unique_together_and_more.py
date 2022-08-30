# Generated by Django 4.1 on 2022-08-15 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_document_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
                ('name', models.TextField(verbose_name='Название документа')),
            ],
            options={
                'verbose_name': 'Тип документа',
                'verbose_name_plural': 'Типы документов',
            },
        ),
        migrations.AlterUniqueTogether(
            name='gtddocument',
            unique_together={('gtd', 'group', 'document')},
        ),
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.documenttype', verbose_name='Id типа документа'),
        ),
    ]