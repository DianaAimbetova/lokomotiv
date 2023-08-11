# Generated by Django 4.2.4 on 2023-08-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheme',
            options={'verbose_name': 'Схема', 'verbose_name_plural': 'Схемы'},
        ),
        migrations.AddField(
            model_name='scheme',
            name='chapter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scheme',
            name='chineese_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='scheme',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]