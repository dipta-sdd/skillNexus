# Generated by Django 4.2.9 on 2024-01-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=' ', max_length=255, unique=True)),
                ('password', models.CharField(default='12345678', max_length=255)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/')),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('role', models.CharField(choices=[('regular_user', 'Regular User'), ('employer', 'Employer'), ('university', 'University')], max_length=50)),
            ],
        ),
    ]
