# Generated by Django 2.2.6 on 2019-10-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191029_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('editor', models.CharField(max_length=250)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('width', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('depth', models.FloatField(default=0)),
            ],
        ),
    ]
