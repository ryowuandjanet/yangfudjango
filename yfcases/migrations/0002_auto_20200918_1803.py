# Generated by Django 3.1 on 2020-09-18 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yfcases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectbuild',
            name='objectBuildTotalPrice',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='總價(NT)'),
        ),
        migrations.AlterField(
            model_name='yfcase',
            name='yfcaseCity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yfcases.city', verbose_name='縣市'),
        ),
        migrations.AlterField(
            model_name='yfcase',
            name='yfcaseTownship',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yfcases.township', verbose_name='鄉鎮區里'),
        ),
    ]
