# Generated by Django 2.2.19 on 2021-02-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teach_id', models.AutoField(primary_key=True, serialize=False)),
                ('teach_name', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
