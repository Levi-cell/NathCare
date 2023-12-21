# Generated by Django 4.2.7 on 2023-12-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0016_alter_especialidade_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='especialidades',
            field=models.ManyToManyField(blank=True, limit_choices_to={'profissional__isnull': True}, to='especialidades.especialidade'),
        ),
    ]