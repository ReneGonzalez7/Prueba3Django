# Generated by Django 4.0.5 on 2022-06-29 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='bio',
            new_name='comentarios',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='web',
        ),
    ]
