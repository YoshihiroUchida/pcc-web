# Generated by Django 3.2.5 on 2022-04-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('pcc_home', '0001_squashed'), ('pcc_home', '0002_home_contents_auth'), ('pcc_home', '0003_home_contents_icon')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PG_contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Home_contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('page', models.CharField(max_length=100)),
                ('auth', models.BooleanField(default=False)),
                ('icon', models.CharField(default='temp', max_length=200)),
            ],
        ),
    ]