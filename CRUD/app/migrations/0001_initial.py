# Generated by Django 4.1.5 on 2023-01-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=50)),
                ('Telefone', models.CharField(max_length=10)),
                ('Senha', models.CharField(max_length=20)),
            ],
        ),
    ]