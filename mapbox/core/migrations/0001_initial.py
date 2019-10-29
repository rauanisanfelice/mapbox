# Generated by Django 2.2.5 on 2019-10-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AREAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_AREA', models.IntegerField()),
                ('DESCRICAO', models.CharField(max_length=150)),
                ('LATITUDE', models.DecimalField(decimal_places=10, max_digits=30)),
                ('LONGITUDE', models.DecimalField(decimal_places=10, max_digits=30)),
                ('ORDEM', models.IntegerField()),
                ('ATIVO', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ENDERECOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LATITUDE', models.DecimalField(decimal_places=10, max_digits=30)),
                ('LONGITUDE', models.DecimalField(decimal_places=10, max_digits=30)),
                ('RAIO', models.IntegerField()),
                ('ATIVO', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LOJAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DESCRICAO', models.CharField(max_length=150)),
                ('LATITUDE', models.DecimalField(decimal_places=10, max_digits=30)),
                ('LONGITUDE', models.DecimalField(decimal_places=10, max_digits=30)),
                ('RAIO', models.IntegerField()),
            ],
        ),
    ]