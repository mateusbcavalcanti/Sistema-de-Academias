# Generated by Django 4.2.10 on 2024-03-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_academia', '0003_rename_nome_aluno_aluno_nome_remove_aluno_cpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('nome', models.TextField(max_length=255, primary_key=True, serialize=False)),
                ('grupo_muscular', models.TextField(max_length=255)),
                ('marca', models.TextField(max_length=255)),
                ('data_compra', models.DateField()),
                ('ult_manutencao', models.DateField()),
                ('fornecedor', models.TextField(max_length=255)),
                ('prazo_manutencao', models.DateField()),
                ('prox_manutencao', models.DateField()),
                ('responsavel', models.TextField(max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='treino',
            name='data_criacao',
            field=models.CharField(default='02/03/2024', max_length=10),
        ),
    ]