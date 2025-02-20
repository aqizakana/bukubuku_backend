# Generated by Django 5.0.7 on 2025-01-09 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('charCountResult', models.IntegerField(blank=True, null=True)),
                ('analyze8labelsResult', models.JSONField(blank=True, null=True)),
                ('koheiduckSentimentScore', models.FloatField(blank=True, null=True)),
                ('koheiduckSentimentLabel', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]
