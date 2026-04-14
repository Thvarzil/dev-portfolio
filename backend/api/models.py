from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    # Basic info
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly name")
    description = models.TextField()
    technology_stack = models.JSONField(default=list)

    # Display metadata
    year = models.IntegerField(null=True, blank=True)
    project_type = models.CharField(max_length=100, blank=True, help_text="e.g. Web App, API / Backend")
    role = models.CharField(max_length=100, blank=True)
    scale = models.CharField(max_length=100, blank=True, help_text="e.g. 10k daily users")
    team = models.CharField(max_length=100, blank=True, help_text="e.g. 4 engineers")
    outcome = models.CharField(max_length=200, blank=True, help_text="e.g. Shipped on time, 40% perf gain")

    # Links
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True, help_text="External demo URL if not hosted here")

    # Hosting configuration
    is_hosted = models.BooleanField(default=False, help_text="Is this project hosted on this infrastructure?")
    has_api = models.BooleanField(default=False, help_text="Does this project have its own backend API?")

    # Display
    featured_image = models.ImageField(upload_to='projects/', blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
