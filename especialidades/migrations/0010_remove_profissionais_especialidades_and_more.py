# Generated by Django 4.2.7 on 2023-12-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0009_alter_profissionais_especialidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profissionais',
            name='especialidades',
        ),
        migrations.AddField(
            model_name='profissionais',
            name='especialidades',
            field=models.ManyToManyField(to='especialidades.especialidades'),
        ),
    ]