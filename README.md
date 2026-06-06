# Key West Shore Excursions

Static planning site for cruise passengers visiting Key West, Florida.

## Build

```bash
npm install
npm run build
```

## Preview locally

```bash
npm run preview
```

Open http://localhost:8912

## Deploy (Cloudflare Pages)

- Framework preset: None
- Build command: `npm run build`
- Build output directory: `.`

Or deploy via Wrangler:

```bash
npm run deploy
```

## Images

```bash
npm run images
```

Replace placeholders listed in `scripts/fetch-key-west-images.py` with your own Key West photography.
