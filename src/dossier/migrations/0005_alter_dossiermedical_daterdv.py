# Generated by Django 5.0.1 on 2024-01-30 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0004_alter_dossiermedical_bilan1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiermedical',
            name='dateRdv',
            field=models.DateField(verbose_name='Date du bilan'),
        ),
    ]