# Generated by Django 4.1.4 on 2022-12-31 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=30)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('passwords', models.CharField(max_length=300)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'genpass',
                'verbose_name_plural': 'liste mots de passe',
                'ordering': ['user'],
            },
        ),
    ]
