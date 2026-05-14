# Portfolio Website

A Django + React portfolio website with multi-project hosting support.

## Architecture

- **Backend:** Django + Django REST Framework
- **Frontend:** React + Vite
- **Deployment:** Single Docker container
- **Static Files:** Whitenoise

## Structure

```
portfolio/
├── backend/              # Django backend
│   ├── portfolio/        # Django settings
│   ├── api/             # Core API (Project model, endpoints)
│   ├── projects/        # Serves side project frontends
│   └── templates/       # HTML templates
├── frontend/
│   ├── portfolio/       # Main portfolio landing page
│   └── projects/        # Side projects directory
├── docker/              # Docker configuration
└── scripts/             # Helper scripts
```

## Quick Start

### Development

1. **Backend Setup:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend/portfolio
   npm install
   ```

3. **Run Development Servers:**
   ```bash
   make dev
   ```
   This starts the Django backend in Docker and the Vite dev server on the host.

4. **Access:**
   - Frontend: http://localhost:5173
   - Backend Admin: http://localhost:8000/admin
   - API: http://localhost:8000/api/

### Production Build

```bash
make build
```

## Adding a New Side Project

1. **Create the frontend:**
   ```bash
   cd frontend/projects
   npm create vite@latest my-project -- --template react
   cd my-project
   npm install
   ```

2. **Configure Vite** (`vite.config.js`):
   ```javascript
   export default defineConfig({
     plugins: [react()],
     build: {
       outDir: path.resolve(__dirname, '../../../backend/staticfiles/projects/my-project'),
       emptyOutDir: true,
     },
     server: {
       port: 5174,  // Different port
       proxy: {
         '/api': {
           target: 'http://localhost:8000',
           changeOrigin: true,
         },
       },
     },
     base: '/static/projects/my-project/',
   })
   ```

3. **Add to database** (via Django admin):
   - Title: "My Project"
   - Slug: "my-project"
   - is_hosted: ✓
   - is_published: ✓

4. **Build and access:**
   ```bash
   cd frontend/projects/my-project && npm run build
   cd ../../../backend && python manage.py collectstatic --noinput
   # Access at http://localhost:8000/projects/my-project/
   ```

## Make Commands

| Command | Description |
|---------|-------------|
| `make dev` | Start backend container + frontend dev server |
| `make up` | Start containers in foreground (backend logs visible) |
| `make down` | Stop containers |
| `make logs` | Tail container logs |
| `make migrate` | Run database migrations |
| `make makemigrations` | Create new migrations |
| `make shell` | Open Django shell in running container |
| `make createsuperuser` | Create a Django superuser |
| `make collectstatic` | Collect static files |
| `make build` | Run production build script |

## Docker

### Development
```bash
docker compose -f docker/docker-compose.yml up
```

### Production
```bash
docker build -f docker/Dockerfile -t portfolio .
docker run -p 8000:8000 portfolio
```

## API Endpoints

- `GET /api/projects/` - List all published projects
- `GET /api/projects/{id}/` - Get project details
- `GET /api/health/` - Health check

## Project Model Fields

- `title` - Project title
- `slug` - URL-friendly identifier
- `description` - Project description
- `technology_stack` - JSON array of technologies
- `github_url` - GitHub repository URL
- `demo_url` - External demo URL
- `is_hosted` - Whether hosted on this infrastructure
- `has_api` - Whether project has backend API
- `featured_image` - Project thumbnail
- `is_published` - Visibility control
- `order` - Display order

## License

MIT
