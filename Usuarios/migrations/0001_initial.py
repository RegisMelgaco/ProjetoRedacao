# Generated by Django 2.0.4 on 2018-04-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('teacher', models.BooleanField(default=False)),
                ('red_pontos', models.IntegerField(default=0)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'), ('P', 'Esta informação é particular')], default='P', max_length=1)),
                ('idade', models.IntegerField(null=True)),
                ('ingresso_ensino_medio', models.DateField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
