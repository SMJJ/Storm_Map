# Generated by Django 3.0.4 on 2020-03-17 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.BigIntegerField(verbose_name='时间戳')),
                ('longitude', models.FloatField(verbose_name='经度')),
                ('latitude', models.FloatField(verbose_name='纬度')),
            ],
            options={
                'verbose_name': '统计信息表',
                'verbose_name_plural': '统计信息表',
                'db_table': 'stat',
            },
        ),
    ]