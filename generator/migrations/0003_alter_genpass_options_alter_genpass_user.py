# Generated by Django 4.1.4 on 2022-12-31 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generator', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genpass',
            options={'ordering': ['user'], 'verbose_name': 'genpass', 'verbose_name_plural': 'liste mots de passe'},
        ),
        migrations.AlterField(
            model_name='genpass',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]