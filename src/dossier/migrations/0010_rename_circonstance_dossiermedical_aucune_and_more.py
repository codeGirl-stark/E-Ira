# Generated by Django 5.0.1 on 2024-02-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0009_dossiermedical_antefamiliaux_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dossiermedical',
            old_name='circonstance',
            new_name='Aucune',
        ),
        migrations.RenameField(
            model_name='dossiermedical',
            old_name='metastase',
            new_name='AutresCir',
        ),
        migrations.RenameField(
            model_name='dossiermedical',
            old_name='totalChir',
            new_name='AutresMeta',
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Cerebrale',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='DecouverteFortuite',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Ganglionaire',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Hepatique',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Metastase',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Nodule',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Oseuse',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='Pulmonaire',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='adp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='curage',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='gnm',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='temps1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='temps2',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
