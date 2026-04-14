from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Project


def portfolio_index(request):
    projects = Project.objects.filter(is_published=True)

    context = {
        'name': 'Lou Le Bohec',
        'role': 'Full Stack Software Engineer · Available for Hire',
        'email': 'louisblebohec@outlook.com',
        'bio': 'Full-stack engineer with seven years across healthcare and enterprise software. I care about the craft — tested code, clean architecture, APIs the next engineer won\'t curse — and use AI tooling deliberately, not as a crutch. Outside the codebase, I run tabletop campaigns for six people, which turns out to be excellent training for organizing complexity and explaining hard things simply.',
        'portrait_url': '',

        'character': {
            'class': 'Full Stack Eng.',
            'location': 'Portland, OR · Remote',
        },

        'languages': [
            {'name': 'English', 'level': 'Native'},
            {'name': 'French', 'level': 'Native'},
        ],

        'traits': [
            {'label': 'Trait', 'text': 'Treats test coverage as a first-class deliverable. Helped bring repositories from 40% to 90%+ coverage.'},
            {'label': 'Trait', 'text': 'Augments output with AI tooling — Claude Code, GitHub Copilot — without losing engineering judgement.'},
            {'label': 'Background', 'text': 'Healthcare systems, billing workflows, enterprise integrations. Comfortable with compliance-adjacent complexity.'},
        ],


        'project_count': projects.count(),

        'projects': [
            {
                'year': p.year,
                'type': p.project_type,
                'title': p.title,
                'description': p.description,
                'tags': p.technology_stack,
                'role': p.role,
                'scale': p.scale,
                'team': p.team,
                'outcome': p.outcome,
                'url': p.demo_url or p.github_url,
            }
            for p in projects
        ],

        'stack': [
            {
                'title': 'Backend',
                'items': [
                    {'name': 'Python',          'level': 3},
                    {'name': 'Django',           'level': 3},
                    {'name': 'REST API Design',  'level': 2},
                    {'name': 'PostgreSQL',       'level': 2},
                    {'name': 'FastAPI',          'level': 2},
                    {'name': 'Redis',            'level': 1},
                ],
            },
            {
                'title': 'Frontend',
                'items': [
                    {'name': 'React',            'level': 3},
                    {'name': 'JavaScript',       'level': 3},
                    {'name': 'HTML / CSS',       'level': 2},
                    {'name': 'TypeScript',       'level': 2},
                ],
            },
            {
                'title': 'Infra & Tooling',
                'items': [
                    {'name': 'Git',              'level': 4},
                    {'name': 'GitHub Actions',   'level': 2},
                    {'name': 'AWS',              'level': 2},
                    {'name': 'Docker',           'level': 2},
                    {'name': 'Kubernetes',       'level': 1},
                ],
            },
            {
                'title': 'Craft',
                'items': [
                    {'name': 'Testing',          'level': 3},
                    {'name': 'Code Review',      'level': 2},
                    {'name': 'Agile / Scrum',    'level': 2},
                ],
            },
        ],

        'social': {
            'github': 'https://www.github.com/thvarzil',
            'linkedin': 'https://www.linkedin.com/in/louis-lebohec',
            'email': 'louisblebohec@outlook.com',
            'cv': '/static/resume.pdf',
        },
    }

    return render(request, 'index.html', context)


@require_http_methods(["GET"])
def project_list(request):
    """Return list of published projects as JSON"""
    projects = Project.objects.filter(is_published=True).values(
        'id', 'title', 'slug', 'description', 'technology_stack',
        'github_url', 'demo_url', 'is_hosted', 'featured_image'
    )
    return JsonResponse(list(projects), safe=False)


@require_http_methods(["GET"])
def project_detail(request, pk):
    """Return single project as JSON"""
    try:
        project = Project.objects.filter(is_published=True).values(
            'id', 'title', 'slug', 'description', 'technology_stack',
            'github_url', 'demo_url', 'is_hosted', 'featured_image'
        ).get(pk=pk)
        return JsonResponse(project)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)


@require_http_methods(["GET"])
def health_check(request):
    """Simple health check endpoint"""
    return JsonResponse({'status': 'ok', 'message': 'API is running'})
