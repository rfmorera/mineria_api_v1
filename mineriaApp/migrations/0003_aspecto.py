# Generated by Django 3.0 on 2020-03-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mineriaApp', '0002_auto_20200319_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspecto',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=500)),
                ('entidades', models.ManyToManyField(to='mineriaApp.Entidad')),
            ],
        ),
    ]
