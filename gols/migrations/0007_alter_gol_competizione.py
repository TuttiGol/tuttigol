# Generated by Django 4.2 on 2023-04-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gols', '0006_alter_gol_stagione'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gol',
            name='competizione',
            field=models.CharField(choices=[('Serie A', 'Serie A'), ('Serie B', 'Serie B'), ('Champions League', 'Champions League'), ('Mondiali 2006', 'Mondiali 2006'), ('Coppa Italia', 'Coppa Italia'), ('Eredivise', 'Eredivise'), ('Europa League', 'Europa League')], max_length=100),
        ),
    ]
