# Generated by Django 4.0.4 on 2022-05-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFormulario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta1', models.CharField(max_length=50)),
                ('pregunta2', models.CharField(max_length=50)),
                ('pregunta3', models.CharField(max_length=50)),
                ('pregunta4', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
