# Generated migration — initial schema

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(help_text='URL-friendly name', unique=True)),
                ('description', models.TextField()),
                ('technology_stack', models.JSONField(default=list)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('project_type', models.CharField(blank=True, help_text='e.g. Web App, API / Backend', max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('scale', models.CharField(blank=True, help_text='e.g. 10k daily users', max_length=100)),
                ('team', models.CharField(blank=True, help_text='e.g. 4 engineers', max_length=100)),
                ('outcome', models.CharField(blank=True, help_text='e.g. Shipped on time, 40% perf gain', max_length=200)),
                ('github_url', models.URLField(blank=True)),
                ('demo_url', models.URLField(blank=True, help_text='External demo URL if not hosted here')),
                ('is_hosted', models.BooleanField(default=False, help_text='Is this project hosted on this infrastructure?')),
                ('has_api', models.BooleanField(default=False, help_text='Does this project have its own backend API?')),
                ('featured_image', models.ImageField(blank=True, upload_to='projects/')),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
