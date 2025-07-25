# Generated by Django 5.2.1 on 2025-06-18 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
                ('bussiness', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('PRIVATE', 'PRIVATE'), ('PUBLIC', 'PUBLIC')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officename', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('PRIVATE', 'PRIVATE'), ('PUBLIC', 'PUBLIC')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardAge', models.IntegerField()),
                ('guardSex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('guardStatus', models.CharField(choices=[('ORDINARY', 'ordinary'), ('ADVANCED', 'advanced')], max_length=10)),
                ('Organization_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.organization')),
                ('Office_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.securityoffice')),
            ],
        ),
        migrations.CreateModel(
            name='ArmedSecurityGuard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('adress', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('ORDINARY', 'ordinary'), ('ADVANCED', 'advanced')], max_length=10)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('worked_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.securityoffice')),
            ],
        ),
    ]
