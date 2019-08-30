# Generated by Django 2.2.4 on 2019-08-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.FileField(upload_to='')),
                ('nome', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('telefone', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(choices=[('project_one', 'Labirinto dos 5 sentidos'), ('project_two', 'Daltonismo'), ('project_three', 'Cinema na caixa'), ('project_four', 'Sistema Digestório')], max_length=50)),
                ('quantidade_participantes', models.CharField(choices=[('3', '3'), ('4', '4')], max_length=2)),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
    ]
