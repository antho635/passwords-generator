# Generated by Django 4.1.1 on 2022-10-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('site vitrine', 'site_vitrine'), ('D', 'Desktop'), ('M', 'Mobile'), ('O', 'Other')], default='site vitrine', max_length=20),
        ),
    ]