# Generated by Django 2.0.4 on 2018-04-23 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Redacao', '0006_auto_20180423_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='redacao',
            old_name='texto',
            new_name='redacao',
        ),
    ]