# Generated by Django 2.2.4 on 2019-10-16 14:00

import api.utils.id_generatory
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=api.utils.id_generatory.id_gen,
                                        editable=False, max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(
                    max_length=100, null=True, unique=True)),
                ('username', models.CharField(db_index=True,
                                              max_length=255, null=True, unique=True)),
                ('email', models.EmailField(
                    db_index=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(default=api.utils.id_generatory.id_gen,
                                        editable=False, max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(default=api.utils.id_generatory.id_gen,
                                        editable=False, max_length=40, primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar', models.URLField()),
                ('deleted_by', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('role', models.ManyToManyField(
                    blank=True, to='authentication.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
