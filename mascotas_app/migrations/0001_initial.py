# Generated by Django 5.1.3 on 2024-11-19 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('codigo', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=100)),
                ('tamaño', models.CharField(max_length=60)),
                ('precio', models.PositiveSmallIntegerField()),
                ('dieta', models.CharField(max_length=60)),
                ('temperamento', models.CharField(max_length=60)),
                ('cuidados', models.CharField(max_length=60)),
                ('edad', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
