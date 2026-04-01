# Shahothon Website Deployment

This website is configured for **automatic GitHub Pages deployment** via:

- `.github/workflows/deploy-shahothon.yml`

## Automatic deploy

A deployment runs automatically when changes are pushed to:

- branch: `work`
- paths: `shahothon-website/**` or the deploy workflow file

## One-time repository setup

In your GitHub repository:

1. Go to **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.

After that, every push to `work` (for website files) deploys the latest version.

## Manual deploy

You can also trigger deployment manually:

1. Open **Actions** tab.
2. Select **Deploy Shahothon Website** workflow.
3. Click **Run workflow**.

## Local preview

From repo root:

```bash
python3 -m http.server 8080 --directory shahothon-website
```

Then open `http://localhost:8080`.
