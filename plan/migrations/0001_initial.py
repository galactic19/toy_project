# Generated by Django 4.0.6 on 2022-07-13 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ltetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Telecom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='telecom', verbose_name='통신사 로고이미지')),
                ('homepage_url', models.URLField(blank=True, verbose_name='통신사 홈페이지')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('discount_money', models.PositiveSmallIntegerField()),
                ('discount_add_money', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ltetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plan.ltetype')),
                ('telecom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.telecom')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at', 'name'],
            },
        ),
    ]
