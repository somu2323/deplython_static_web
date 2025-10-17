Deploying this project to Cloudflare Pages (static)\n\nThis Django project is effectively a static portfolio page (no dynamic DB-driven pages). Cloudflare Pages can host a static site by exporting the rendered templates and static assets into a `dist/` folder.\n\nSteps to use the included exporter and deploy to Cloudflare Pages:\n\n1. Build the static `dist/` locally:\n\n```powershell
# from project root (where export_static.py lives)
python export_static.py
# This will create a `dist/` directory containing `index.html` and `static/` assets.
```\n\n2. Preview locally (optional):\n\n```powershell
# Use a simple HTTP server to preview
python -m http.server 8000 -d dist
# or (PowerShell)
Start-Process -NoNewWindow -FilePath python -ArgumentList '-m','http.server','8000','-d','dist'
```\n\n3. Deploy to Cloudflare Pages:\n\n- Push your repo to GitHub.com (or connect your Git provider to Cloudflare Pages).\n- In Cloudflare Pages, create a new project and connect your repository.\n- Set the "Build command" to:\n\n```
python export_static.py
```
\n- Set the "Build output directory" (Publish directory) to:\n\n```
dist
```
\n- (Optional) Set Python version in environment if needed (Cloudflare Pages builder images provide multiple runtimes); typically you don't need extra packages for this simple exporter.\n\nNotes and caveats:\n- This exporter does a minimal transformation of Django `{% static %}` tags into `static/` paths. If you add more templates or use template inheritance and context variables, you may need a more robust export (for example, using Django's template engine or a dedicated static-site exporter).\n- If your site later needs dynamic server-side features (forms, auth, DB), Cloudflare Pages alone won't run Django — you'd need serverless functions or host Django on a separate server and use Pages for the static front-end.\n- For improved caching and compression, Cloudflare Pages + Cloudflare CDN will handle requests; you can also add custom headers in Cloudflare rules.
