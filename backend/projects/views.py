from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from api.models import Project


class ProjectDetailView(TemplateView):
    template_name = 'project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']

        # Verify project exists and is published
        project = get_object_or_404(
            Project,
            slug=slug,
            is_published=True,
            is_hosted=True
        )

        context['project'] = project
        context['project_slug'] = slug
        return context
