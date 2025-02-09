# Generated by Django 5.1.5 on 2025-02-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0010_globalassets'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_head', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, choices=[('Agent', 'Agent')], max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('unique_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
    ]
