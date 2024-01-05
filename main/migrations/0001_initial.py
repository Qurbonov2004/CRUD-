# Generated by Django 5.0 on 2024-01-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(null=True)),
                ('is_activate', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mashgulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mashgulot_nomi', models.CharField(max_length=255)),
                ('davomiyligi', models.CharField(max_length=25)),
                ('boshlainish_vaqti', models.DateField()),
                ('tugashsh_vaqti', models.DateField()),
                ('mashgulot_icon', models.ImageField(upload_to='')),
                ('kuni', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.ImageField(upload_to='')),
                ('service1_name', models.CharField(max_length=55)),
                ('about_service', models.TextField()),
            ],
            options={
                'verbose_name': 'xizmatlar',
                'verbose_name_plural': 'xizmatlar',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('haqida', models.TextField()),
            ],
        ),
    ]
