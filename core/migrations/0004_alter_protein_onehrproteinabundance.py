# Generated by Django 4.1 on 2022-08-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_protein_onehrproteinabundance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='OneHrProteinAbundance',
            field=models.BigIntegerField(),
        ),
    ]
