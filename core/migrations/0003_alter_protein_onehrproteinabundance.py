# Generated by Django 4.1 on 2022-08-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_protein_fivehrproteinabundance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='OneHrProteinAbundance',
            field=models.IntegerField(),
        ),
    ]
