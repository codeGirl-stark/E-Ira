# Generated by Django 5.0.1 on 2024-02-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0007_alter_dossiermedical_activitecumule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiermedical',
            name='activiteCumule',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dossiermedical',
            name='nbrCure',
            field=models.IntegerField(null=True),
        ),
    ]
