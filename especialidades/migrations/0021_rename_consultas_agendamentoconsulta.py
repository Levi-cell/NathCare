# Generated by Django 4.2.7 on 2023-12-18 00:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('especialidades', '0020_rename_consultas_profissional_especialidades_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consultas',
            new_name='AgendamentoConsulta',
        ),
    ]
