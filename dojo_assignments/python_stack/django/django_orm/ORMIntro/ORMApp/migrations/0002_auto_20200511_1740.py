# Generated by Django 2.2.4 on 2020-05-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORMApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketballplayer',
            name='first_game',
            field=models.DateField(),
        ),
    ]