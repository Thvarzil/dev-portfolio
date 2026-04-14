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
   # Option 1: Using the dev script
   ./scripts/dev.sh

   # Option 2: Manual (two terminals)
   # Terminal 1
   cd backend && python manage.py runserver

   # Terminal 2
   cd frontend/portfolio && npm run dev
   ```

4. **Access:**
   - Frontend: http://localhost:5173
   - Backend Admin: http://localhost:8000/admin
   - API: http://localhost:8000/api/

### Production Build

```bash
./scripts/build.sh
cd backend && python manage.py runserver
# Visit http://localhost:8000
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

## Docker

### Development
```bash
docker-compose -f docker/docker-compose.yml up
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
