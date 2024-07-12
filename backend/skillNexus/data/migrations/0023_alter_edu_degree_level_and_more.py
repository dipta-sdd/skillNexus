# Generated by Django 4.2 on 2024-05-03 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_remove_edu_degree_level_edu_degree_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu_degree',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.edu_level'),
        ),
        migrations.RemoveField(
            model_name='edu_group_or_major',
            name='degree',
        ),
        migrations.AlterField(
            model_name='project',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects_participated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='edu_group_or_major',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.edu_degree'),
        ),
    ]
