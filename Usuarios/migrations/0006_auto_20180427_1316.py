# Generated by Django 2.0.4 on 2018-04-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_auto_20180423_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='primeiro_nome',
            field=models.CharField(default='sem', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='segundo_nome',
            field=models.CharField(default='nome', max_length=30),
            preserve_default=False,
        ),
    ]
