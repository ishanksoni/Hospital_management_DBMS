# Generated by Django 3.0.6 on 2020-05-31 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_auto_20200531_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='Pre_medical_history',
            new_name='cmnt',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='Tests',
            new_name='dis',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='comment',
            new_name='history',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='discreption',
            new_name='medic',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='init_observation',
            new_name='observ',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='medication',
            new_name='test',
        ),
        migrations.AlterModelTable(
            name='report',
            table='report',
        ),
    ]
