# Generated by Django 2.0.4 on 2018-05-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Redacao', '0014_auto_20180502_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redacao',
            name='usuarios',
        ),
    ]
