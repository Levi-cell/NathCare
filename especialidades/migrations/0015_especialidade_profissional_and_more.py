# Generated by Django 4.2.7 on 2023-12-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0014_remove_profissionalespecialidade_especialidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Cardiologia', 'Cardiologia'), ('Dermatologia', 'Dermatologia'), ('Ortopedia', 'Ortopedia')], max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('especialidades', models.ManyToManyField(blank=True, to='especialidades.especialidade')),
            ],
        ),
        migrations.RemoveField(
            model_name='profissionalespecialidade',
            name='especialidade',
        ),
        migrations.RemoveField(
            model_name='profissionalespecialidade',
            name='profissional',
        ),
        migrations.DeleteModel(
            name='Especialidades',
        ),
        migrations.DeleteModel(
            name='Profissionais',
        ),
        migrations.DeleteModel(
            name='ProfissionalEspecialidade',
        ),
    ]
