# Generated by Django 4.2.7 on 2023-12-19 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_newuser_cpf_newuser_cpf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewUser',
        ),
    ]
