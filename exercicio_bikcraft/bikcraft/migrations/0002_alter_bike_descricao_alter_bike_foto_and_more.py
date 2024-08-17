# Generated by Django 5.0.6 on 2024-06-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikcraft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='bikcraft/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='modelo',
            field=models.CharField(max_length=255, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='preco',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='contados',
            name='email',
            field=models.CharField(max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contados',
            name='mensagem',
            field=models.TextField(verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='contados',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
    ]
