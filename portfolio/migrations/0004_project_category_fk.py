# Generated by Django 4.1.1 on 2022-10-31 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_category_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
        ),
    ]
