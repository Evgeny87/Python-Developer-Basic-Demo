# Generated by Django 4.1 on 2023-01-06 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, max_length=2000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_django_app.user')),
            ],
        ),
    ]