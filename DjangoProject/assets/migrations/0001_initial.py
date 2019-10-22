# Generated by Django 2.2.4 on 2019-08-27 16:56

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.EnumType')),
                ('item', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UriElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=128, unique=True)),
                ('schema', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('parent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                  related_name='children', to='assets.AssetType')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content_ids', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('content_cache', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('invalidation_list', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(),
                                                                                blank=True, null=True, size=None)),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets',
                                        to='assets.AssetType')),
                ('revision_chain', models.ForeignKey(blank=True, null=True,
                                                     on_delete=django.db.models.deletion.SET_NULL,
                                                     related_name='new_version', to='assets.Asset')),
            ],
        ),
    ]
