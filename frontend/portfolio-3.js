const PROJECTS = [
  {
    year: 2024, type: "Web App", title: "Healthcare Dashboard",
    desc: "Real-time patient data dashboard for clinical staff. Designed for compliance-constrained environments with strict data handling requirements.",
    tags: ["React","Django","PostgreSQL","Redis"],
    role: "Lead Engineer", scale: "10k daily users", team: "4 engineers",
    outcome: "Shipped on time, 40% performance gain", url: "#"
  },
  {
    year: 2023, type: "API / Backend", title: "Enterprise API Platform",
    desc: "Internal REST API layer consolidating legacy data sources for a large enterprise client. Comprehensive test coverage and OpenAPI documentation.",
    tags: ["Python","FastAPI","PostgreSQL","Docker"],
    role: "Backend Engineer", scale: "Internal tooling", team: "3 engineers",
    outcome: "Replaced 5 brittle integrations with one stable service", url: "#"
  },
  {
    year: 2023, type: "Side Project", title: "OSR Dungeon Ref Tools",
    desc: "Browser-based GM reference toolkit for old-school tabletop RPG. Random generators, encounter tables, and session notes — all local-first.",
    tags: ["React","Vite","TypeScript"],
    role: "Solo", scale: "Personal project", team: "Solo",
    outcome: "Used weekly in active campaigns", url: "https://github.com/thvarzil"
  }
];

const STACK = [
  { t: "Backend",
    skills: ["Python","Django","Django ORM","REST API Design","PostgreSQL","FastAPI","Redis","SQLite","Celery"] },
  { t: "Frontend",
    skills: ["React","JavaScript","TypeScript","HTML / CSS","Vite","Tailwind CSS"] },
  { t: "Infra & Tooling",
    skills: ["Git","GitHub Actions","Docker","AWS","Kubernetes","Whitenoise","CI/CD","Linux"] },
  { t: "Craft",
    skills: ["Testing","TDD","Code Review","Agile / Scrum","OpenAPI","Technical Writing"] }
];

const pl = document.getElementById('proj-list');
PROJECTS.forEach((p, i) => {
  const el = document.createElement('div');
  el.className = 'pe s' + (i + 1);
  el.innerHTML = `
    <div class="pbl"><span class="pyr">${p.year}</span></div>
    <div class="pb">
      <div class="pt">
        <h3 class="ptitle">${p.title}</h3>
        <span class="ptag">${p.type}</span>
      </div>
      <p class="pdesc">${p.desc}</p>
      <div class="pmeta">
        <span class="pmi"><span class="pml">Role</span><span class="pmv">${p.role}</span></span>
        <span class="pmi"><span class="pml">Scale</span><span class="pmv">${p.scale}</span></span>
        <span class="pmi"><span class="pml">Team</span><span class="pmv">${p.team}</span></span>
      </div>
      <p class="pout">✦ ${p.outcome}</p>
      <div class="tags">${p.tags.map(t => `<span class="tag">${t}</span>`).join('')}</div>
      ${p.url && p.url !== '#' ? `<a href="${p.url}" class="plink" target="_blank" rel="noopener">View →</a>` : ''}
    </div>`;
  pl.appendChild(el);
});

const sg = document.getElementById('stack-grid');
STACK.forEach((c, i) => {
  const el = document.createElement('div');
  el.className = 'scat s' + (i + 1);
  const names = c.skills.map(s => '<span class="skn">' + s + '</span>').join('');
  el.innerHTML = '<div class="sch">' + c.t + '</div><div class="sk-names">' + names + '</div>';
  sg.appendChild(el);
});

document.getElementById('yr').textContent = new Date().getFullYear();

const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('vis'); obs.unobserve(e.target); }
  });
}, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.rev, .pe, .con-block').forEach(el => obs.observe(el));
setTimeout(() => document.querySelector('.hero-inner').classList.add('vis'), 80);
