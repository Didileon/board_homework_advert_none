# Generated by Django 5.0.6 on 2024-07-20 12:49

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DateAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(verbose_name='url')),
            ],
            options={
                'verbose_name': 'Срок',
                'verbose_name_plural': 'Сроки',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FilterAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='config.category', verbose_name='Родитель')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема')),
                ('description', models.TextField(max_length=10000, verbose_name='Объявление')),
                ('file', models.FileField(blank=True, null=True, upload_to='board/', verbose_name='Файл')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('rating', models.SmallIntegerField(default=0, verbose_name='Лайки')),
                ('images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.gallery', verbose_name='Изображения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.category', verbose_name='Категория')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.dateadvert', verbose_name='Срок')),
                ('filters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.filteradvert', verbose_name='Фильтр')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=10000, verbose_name='Объявление')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('rating', models.SmallIntegerField(default=0, verbose_name='Комментарий')),
                ('commentAdvert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.advert')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
