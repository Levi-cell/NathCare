# Generated by Django 4.2.7 on 2023-12-17 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0010_remove_profissionais_especialidades_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profissionais',
            name='especialidades',
        ),
        migrations.DeleteModel(
            name='Especialidades',
        ),
        migrations.DeleteModel(
            name='Profissionais',
        ),
    ]
