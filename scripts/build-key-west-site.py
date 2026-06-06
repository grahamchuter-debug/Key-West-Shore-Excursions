#!/usr/bin/env python3
"""Generate Key West Shore Excursions static site files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://keywestshoreexcursions.com"
SITE = "Key West Shore Excursions"
DATE = "2026-06-06"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700"
    "&family=Nunito+Sans:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(124, 45, 18, 0.85) 0%, "
    "rgba(234, 88, 12, 0.78) 45%, rgba(249, 115, 22, 0.65) 100%)"
)
ACCENT = "text-amber-200"

HOME_HERO = "images/hero-key-west.png"
HOME_HERO_ALT = "Colourful Duval Street in Key West Old Town with historic wooden buildings visited by cruise passengers"
BEST_IMG = "images/best-key-west-excursions.png"
BEST_ALT = "Best Key West shore excursions including sightseeing snorkelling and sunset sailing"
PORT_IMG = "images/key-west-cruise-port.png"
PORT_ALT = "Cruise ship visiting Key West cruise port in Florida"
ONE_DAY_IMG = "images/one-day-key-west.png"
ONE_DAY_ALT = "One day in Key West for cruise passengers exploring Old Town"
WALK_IMG = "images/walk-from-port.png"
WALK_ALT = "Cruise passengers walking from Key West cruise port into Old Town"
SOUTH_IMG = "images/southernmost-point.png"
SOUTH_ALT = "Southernmost Point buoy in Key West Florida"
DUVAL_IMG = "images/duval-street.png"
DUVAL_ALT = "Duval Street in Key West with shops bars and restaurants"
HEMINGWAY_IMG = "images/hemingway-house.png"
HEMINGWAY_ALT = "Ernest Hemingway Home and Museum in Key West"
CONCH_IMG = "images/conch-train.png"
CONCH_ALT = "Conch Tour Train sightseeing excursion in Key West"
TROLLEY_IMG = "images/key-west-trolley.png"
TROLLEY_ALT = "Key West trolley tour through Old Town"
SNORKEL_IMG = "images/key-west-snorkelling.png"
SNORKEL_ALT = "Snorkelling tour in Key West with coral reef and clear water"
DOLPHIN_IMG = "images/key-west-dolphin.png"
DOLPHIN_ALT = "Dolphin watching excursion from Key West"
SUNSET_IMG = "images/key-west-sunset-sailing.png"
SUNSET_ALT = "Sunset sailing excursion in Key West Florida"
TORTUGAS_IMG = "images/dry-tortugas.png"
TORTUGAS_ALT = "Dry Tortugas and Fort Jefferson excursion from Key West"
FAMILY_IMG = "images/key-west-family.png"
FAMILY_ALT = "Family friendly Key West shore excursion from the cruise port"
FAQ_IMG = "images/key-west-faq.png"
FAQ_ALT = "Cruise passengers exploring Key West Florida"
INTRO_IMG = "images/key-west-intro.png"
INTRO_ALT = "Southernmost Point buoy in Key West Florida visited by cruise passengers"


def page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    hero: str,
    content: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: bool = True,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_attr = '\n  data-trust-strip="partials/trust-strip.html"' if trust else ""
    content_file = content if content.startswith("content/") else f"content/{content}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{data_page}"
  data-base=""
  data-hero="{hero}"
  data-content="{content_file}"{trust_attr}
>

  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>

  <script src="js/site.js"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    walking: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Walking Required</dt><dd>{walking}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def _hero_wave() -> str:
    return '<div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'


def _hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
    tags_html = ""
    if tags:
        tags_html = '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">' + "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
            for t in tags
        ) + "</div>"
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-amber-300 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {_hero_wave()}
</section>"""


def _internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Key West guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="key-west-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-key-west-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="one-day-in-key-west.html" class="text-ocean-600 hover:text-ocean-800 font-medium">One Day</a>
    <span class="text-gray-300">·</span>
    <a href="can-you-walk-key-west-from-cruise-port.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Walk From Port</a>
    <span class="text-gray-300">·</span>
    <a href="southernmost-point-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Southernmost Point</a>
    <span class="text-gray-300">·</span>
    <a href="duval-street-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Duval Street</a>
    <span class="text-gray-300">·</span>
    <a href="hemingway-house-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Hemingway House</a>
    <span class="text-gray-300">·</span>
    <a href="key-west-conch-train-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Conch Train</a>
    <span class="text-gray-300">·</span>
    <a href="key-west-trolley-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Trolley</a>
    <span class="text-gray-300">·</span>
    <a href="key-west-snorkelling-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Snorkelling</a>
    <span class="text-gray-300">·</span>
    <a href="key-west-dolphin-watching-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Dolphins</a>
    <span class="text-gray-300">·</span>
    <a href="key-west-sunset-sailing.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Sunset Sailing</a>
    <span class="text-gray-300">·</span>
    <a href="key-west-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def _comparison_section() -> str:
    rows = [
        ("Walkable Old Town", "2–6 hrs", "Independent exploring on foot", "Moderate — flat streets", "can-you-walk-key-west-from-cruise-port.html"),
        ("Southernmost Point", "1–2 hrs", "Iconic photo stop", "Moderate — 1.5 mi from port", "southernmost-point-tours.html"),
        ("Duval Street", "2–4 hrs", "Shops, bars &amp; key lime pie", "Moderate — main strip", "duval-street-guide.html"),
        ("Conch Train", "1.5–2 hrs", "Guided Old Town highlights", "Low — sit &amp; ride", "key-west-conch-train-tours.html"),
        ("Trolley Tour", "1.5–2 hrs", "Hop-on hop-off sightseeing", "Low — sit &amp; ride", "key-west-trolley-tours.html"),
        ("Snorkelling", "2–3 hrs", "Reef &amp; clear Florida Keys water", "Moderate — boat &amp; swim", "key-west-snorkelling-tours.html"),
        ("Dolphin Watching", "2–3 hrs", "Wild dolphins near Key West", "Low to moderate — boat", "key-west-dolphin-watching-tours.html"),
        ("Sunset Sailing", "2–3 hrs", "Harbour sunset on a sailboat", "Low — boat ride", "key-west-sunset-sailing.html"),
        ("Dry Tortugas", "Full day", "Fort Jefferson &amp; remote reef", "Moderate — ferry or seaplane", "dry-tortugas-excursions.html"),
    ]
    body = ""
    for name, dur, best, walking, link in rows:
        body += f"""<tr class="border-b border-keys-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{walking}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-keys-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Key West Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Many cruise passengers explore Key West independently on foot — but guided Conch Train, trolley, snorkel and sunset tours help you cover more in a short port call. Match your time ashore to the option that fits.</p>
  <div class="overflow-x-auto rounded-3xl border border-keys-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Walking Required</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-keys-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="6–10 hours (typical)",
        best_for="Old Town walking, Southernmost Point, Duval Street, Conch Train",
        walking="Varies — see comparison table",
        family="Excellent with age-appropriate picks",
        return_ship="Operators usually allow 60–90 min buffer",
        popular="Walking tours, Conch Train, snorkelling, sunset sailing",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def _content_excursion_page(
    intro: str,
    bullets: list[str],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-amber-300 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Key West Cruise Port · Florida Keys</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Key West Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Walk from your ship into colourful Old Town — Southernmost Point, Duval Street, Hemingway House and Mallory Square are all within reach. Or book a Conch Train, snorkel trip, dolphin watch or sunset sail timed for your port call.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-key-west-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="can-you-walk-key-west-from-cruise-port.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Walk From Port</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Southernmost Point</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Duval Street</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Walkable Old Town</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Conch Train</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Sunset Sailing</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def _content_home() -> str:
    cards = _card_grid([
        (SOUTH_IMG, SOUTH_ALT, "Southernmost Point", "The famous buoy marking the southernmost spot in the continental US — a must-see photo stop.", "southernmost-point-tours.html", "Southernmost Point"),
        (DUVAL_IMG, DUVAL_ALT, "Duval Street", "Shops, bars, galleries and key lime pie on Key West's main strip.", "duval-street-guide.html", "Duval Street"),
        (CONCH_IMG, CONCH_ALT, "Conch Train", "Open-air train covering Old Town highlights when time is short.", "key-west-conch-train-tours.html", "Conch Train"),
        (SUNSET_IMG, SUNSET_ALT, "Sunset Sailing", "Harbour sunset on a sailboat — classic Key West evening.", "key-west-sunset-sailing.html", "Sunset Sailing"),
    ])
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Walkable Cruise Port</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Guests<br/><span class="text-ocean-600">Love Key West</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">Key West is one of the most walkable cruise ports in Florida — colourful Old Town streets, the Southernmost Point buoy, Duval Street and Mallory Square are all reachable on foot. Conch Train, trolley tours, snorkelling and sunset sails fit a typical <strong>6–10 hour</strong> port call without long transfers.</p>
        <a href="best-key-west-shore-excursions.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Browse All Excursions</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top Key West Experiences</h2></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Key West Port Day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="key-west-cruise-port-guide.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="key-west-faq.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">FAQ</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid([
        (CONCH_IMG, CONCH_ALT, "Conch Train", "Guided open-air train through Old Town landmarks.", "key-west-conch-train-tours.html", "Conch Train"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling", "Reef trips in clear Florida Keys water.", "key-west-snorkelling-tours.html", "Snorkelling"),
        (DOLPHIN_IMG, DOLPHIN_ALT, "Dolphin Watching", "Wild dolphin encounters on harbour boat trips.", "key-west-dolphin-watching-tours.html", "Dolphins"),
        (TORTUGAS_IMG, TORTUGAS_ALT, "Dry Tortugas", "Fort Jefferson day trip for longer port calls.", "dry-tortugas-excursions.html", "Dry Tortugas"),
    ])
    snap = _snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Key West Shore Excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Many guests walk Old Town independently — organised tours at the <strong>Key West cruise port</strong> help you see more before all aboard.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_port() -> str:
    snap = _snapshot_default(
        walking="Low at terminal; moderate in Old Town",
        popular="Walking, Conch Train, snorkel boats, sunset sails",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 leading-relaxed text-sm">Ships dock at the <strong>Key West cruise port</strong> on Mallory Square or the Outer Mole — both put you minutes from Old Town on a typical <strong>6–10 hour</strong> call.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-keys-100"><h3 class="font-display font-bold text-lg mb-2">Mallory Square Pier</h3><p class="text-gray-600">Steps from Mallory Square sunset celebrations, Duval Street and harbourfront shops — the most walkable dock for cruise passengers.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-keys-100"><h3 class="font-display font-bold text-lg mb-2">Outer Mole Pier</h3><p class="text-gray-600">A slightly longer walk or short shuttle to Old Town. Conch Train, trolley and taxi stands meet ships here.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-3 gap-6 text-sm">
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">US dollar (USD). Cards and cash widely accepted at the port and in Old Town.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English throughout Key West. Port staff and tour operators speak clear English.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Walk Old Town; Conch Train and trolley for sightseeing; taxis and pedicabs for Southernmost Point.</p></div>
      </div>
      <p class="text-center mt-8"><a href="can-you-walk-key-west-from-cruise-port.html" class="text-ocean-600 font-semibold text-sm">Can you walk from the port? →</a> · <a href="one-day-in-key-west.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(best_for="Morning walk + Conch Train or snorkel afternoon")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">Sample timeline for a <strong>6–10 hour</strong> Key West call. Adjust for your ship's actual times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Key West Port Day</h2>
      <ol class="space-y-4 text-sm">
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-keys-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Walk into Old Town</strong><p class="text-gray-600 mt-1">Head straight from the pier toward Duval Street — coffee and key lime pie await.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-keys-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>Conch Train or Southernmost Point</strong><p class="text-gray-600 mt-1">Ride the Conch Train for an overview, or walk/taxi to the Southernmost Point buoy.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-keys-100"><span class="font-bold text-ocean-600 shrink-0">11:30</span><div><strong>Hemingway House</strong><p class="text-gray-600 mt-1">Tour Ernest Hemingway's home and famous six-toed cats — book ahead on busy days.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-keys-100"><span class="font-bold text-ocean-600 shrink-0">13:00</span><div><strong>Lunch on Duval Street</strong><p class="text-gray-600 mt-1">Fresh seafood, conch fritters or key lime pie at a harbourfront spot.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-keys-100"><span class="font-bold text-ocean-600 shrink-0">15:00</span><div><strong>Snorkel or Mallory Square</strong><p class="text-gray-600 mt-1">Afternoon reef snorkel trip, or stroll back to Mallory Square for street performers.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-keys-100"><span class="font-bold text-ocean-600 shrink-0">17:00</span><div><strong>Return to ship</strong><p class="text-gray-600 mt-1">Allow margin before published all-aboard — the pier is a short walk from Old Town.</p></div></li>
      </ol>
      <div class="mt-10">{_internal_links()}</div>
    </div></section>"""


def _content_walk() -> str:
    return _content_excursion_page(
        "Key West is one of the most walkable cruise ports in the United States — colourful Old Town streets start minutes from the gangway. Duval Street, Mallory Square and many shops need no taxi. Southernmost Point and Hemingway House are a longer flat walk or quick pedicab ride.",
        [
            "Mallory Square pier: Duval Street in 5–10 minutes on foot.",
            "Outer Mole pier: 15–20 minute walk or short shuttle to Old Town.",
            "Flat, grid-layout streets suit independent exploring.",
            "Guided Conch Train or trolley helps if time is tight.",
        ],
        dict(
            best_for="Independent explorers and first-time visitors",
            walking="Moderate — 1–3 miles for main sights",
            popular="Self-guided Old Town walk, Duval Street, Mallory Square",
        ),
        WALK_IMG,
        WALK_ALT,
    )


def _content_southernmost() -> str:
    return _content_excursion_page(
        "The Southernmost Point buoy is Key West's most photographed landmark — a striped concrete buoy marking the southernmost spot in the continental United States. It sits at the corner of Whitehead and South streets, about 1.5 miles from the cruise port.",
        [
            "20–30 minute walk from Mallory Square pier.",
            "Taxi or pedicab available if you prefer not to walk.",
            "Often included on Conch Train and trolley routes.",
            "Go early to avoid the longest photo queues.",
        ],
        dict(
            best_for="Photo seekers and landmark hunters",
            walking="Moderate — 1.5 mi from port or ride",
            popular="Southernmost Point tours, Conch Train combos",
        ),
        SOUTH_IMG,
        SOUTH_ALT,
    )


def _content_duval() -> str:
    return _content_excursion_page(
        "Duval Street is the heart of Key West — a mile-long strip of colourful wooden buildings, open-air bars, art galleries, boutiques and key lime pie shops. From the cruise port it is one of the easiest walks ashore.",
        [
            "5–15 minutes from either Key West pier.",
            "Best explored on foot — no tour required.",
            "Lunch spots, live music and souvenir shops throughout.",
            "Pair with Mallory Square for sunset if your ship stays late.",
        ],
        dict(
            best_for="Shoppers, food lovers and casual strollers",
            walking="Moderate — flat main strip",
            popular="Self-guided walk, pub crawl, food tours",
        ),
        DUVAL_IMG,
        DUVAL_ALT,
    )


def _content_hemingway() -> str:
    return _content_excursion_page(
        "The Ernest Hemingway Home and Museum preserves the author's 1851 Spanish Colonial estate — famous for its six-toed cats, writing studio and lush gardens. It sits in Old Town, a pleasant walk or short ride from the cruise port.",
        [
            "Self-guided audio tours run throughout the day.",
            "15–20 minute walk from Mallory Square pier.",
            "Book timed entry on busy cruise days.",
            "Often combined with Conch Train or walking tours.",
        ],
        dict(
            best_for="Literature fans and history lovers",
            walking="Moderate — walk or short taxi",
            popular="Hemingway House tours, Old Town walking tours",
        ),
        HEMINGWAY_IMG,
        HEMINGWAY_ALT,
    )


def _content_conch() -> str:
    return _content_excursion_page(
        "The Conch Tour Train has carried visitors through Key West since 1958 — an open-air sightseeing train covering Old Town highlights including Southernmost Point, Hemingway House area and historic architecture with live narration.",
        [
            "90-minute loop with hop-off options on some tickets.",
            "Departs near the cruise port and Mallory Square.",
            "Low walking — ideal for hot days or limited mobility.",
            "Fits easily into a 6–10 hour port call.",
        ],
        dict(
            best_for="First-time visitors short on time",
            walking="Low — sit-and-ride sightseeing",
            popular="Conch Train tours, train + snorkel combos",
        ),
        CONCH_IMG,
        CONCH_ALT,
    )


def _content_trolley() -> str:
    return _content_excursion_page(
        "Key West trolley tours offer hop-on hop-off sightseeing through Old Town — colourful open-sided vehicles with guided commentary covering Duval Street, the harbour and landmark stops at your own pace.",
        [
            "Multiple daily departures from near the port.",
            "Hop off at Southernmost Point, Duval Street and more.",
            "Less walking than a full self-guided day.",
            "Good alternative to the Conch Train.",
        ],
        dict(
            best_for="Sightseers who want flexibility",
            walking="Low — ride with optional stops",
            popular="Hop-on hop-off trolley, Old Town loops",
        ),
        TROLLEY_IMG,
        TROLLEY_ALT,
    )


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "Key West sits at the edge of the Florida Keys reef tract — snorkel tours visit coral patches and wrecks in clear Atlantic and Gulf water. Catamaran trips depart from the harbour with gear included and cruise-timed returns.",
        [
            "Half-day trips fit most 6–10 hour port schedules.",
            "Beginners welcome — flotation aids often available.",
            "Use reef-safe sunscreen or a rash guard.",
            "Calm mornings offer the best visibility.",
        ],
        dict(
            best_for="Reef swimmers and marine life fans",
            walking="Low at port — moderate on boat",
            popular="Reef snorkel catamarans, combo dolphin snorkel",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_dolphin() -> str:
    return _content_excursion_page(
        "Dolphin watching tours from Key West search the harbour and nearby waters for wild Atlantic bottlenose dolphins — playful pods often surface near boats. Trips combine wildlife viewing with coastal scenery and sometimes a snorkel stop.",
        [
            "2–3 hour trips fit standard port calls.",
            "Family-friendly with shade on most vessels.",
            "Wildlife sightings vary — no guarantees.",
            "Morning departures allow afternoon Old Town time.",
        ],
        dict(
            best_for="Wildlife lovers and families",
            walking="Low — boat excursion",
            popular="Dolphin watch boats, dolphin and snorkel combos",
        ),
        DOLPHIN_IMG,
        DOLPHIN_ALT,
    )


def _content_sunset() -> str:
    return _content_excursion_page(
        "Sunset sailing is a Key West tradition — schooners and catamarans depart the harbour for golden-hour views over the Gulf. Choose this when your ship has a late departure and you have already seen Old Town on foot.",
        [
            "2–3 hours on the water with drinks often included.",
            "Best on ships departing 18:00 or later.",
            "Book early — popular on cruise days.",
            "Pair with a morning Conch Train or walking tour.",
        ],
        dict(
            best_for="Romantic evenings and classic Key West vibes",
            walking="Low — board at harbour",
            popular="Sunset schooner sails, catamaran cruises",
        ),
        SUNSET_IMG,
        SUNSET_ALT,
    )


def _content_tortugas() -> str:
    return _content_excursion_page(
        "Dry Tortugas National Park lies 70 miles west of Key West — Fort Jefferson, a massive 19th-century coastal fortress, sits on a remote island surrounded by pristine reef. Ferry and seaplane day trips depart Key West harbour but need a full port day.",
        [
            "Full-day trip — only for 8+ hour port calls.",
            "Ferry takes ~2.5 hours each way.",
            "Snorkelling around the fort moat included on most trips.",
            "Book weeks ahead on peak cruise season dates.",
        ],
        dict(
            best_for="History buffs on long port days",
            walking="Moderate — fort exploration on island",
            popular="Yankee Freedom ferry, seaplane day trips",
            time_in_port="8+ hours required",
            return_ship="Fixed ferry schedule — verify ship departure",
        ),
        TORTUGAS_IMG,
        TORTUGAS_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family excursions in Key West favour walkable Old Town, the Conch Train, gentle snorkel trips and dolphin watching. Flat streets and short distances make independent exploring easy with children — two well-paced stops beat three rushed attractions.",
        [
            "Conch Train engages kids without long walks.",
            "Hemingway House cats are a hit with children.",
            "Snorkel trips often welcome ages 6+.",
            "Key lime pie stop on Duval Street is a must.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Excellent with age-appropriate tour choice",
            popular="Conch Train, dolphin watch, family snorkel",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-keys-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Key West?</summary>
        <p class="mt-4 text-sm text-gray-500">Most Key West calls are 6 to 10 hours. Walking Old Town plus one organised tour fits comfortably with return buffer.</p></details>
      <details class="faq-item rounded-2xl border border-keys-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Can you walk from the Key West cruise port?</summary>
        <p class="mt-4 text-sm text-gray-500">Yes — Duval Street and Mallory Square are 5–15 minutes on foot from the Mallory Square pier. Southernmost Point is about 1.5 miles.</p></details>
      <details class="faq-item rounded-2xl border border-keys-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Do I need a tour or can I explore on my own?</summary>
        <p class="mt-4 text-sm text-gray-500">Many passengers explore independently — Key West is very walkable. Conch Train, trolley, snorkel and sunset tours help when time is short.</p></details>
      <details class="faq-item rounded-2xl border border-keys-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What are the must-see sights?</summary>
        <p class="mt-4 text-sm text-gray-500">Southernmost Point buoy, Duval Street, Ernest Hemingway Home, Mallory Square and key lime pie. Conch Train covers highlights quickly.</p></details>
      <details class="faq-item rounded-2xl border border-keys-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship tours guarantee the vessel waits if the operator is late. Reputable Key West operators plan returns with buffer — confirm policies before booking ashore.</p></details>
      <details class="faq-item rounded-2xl border border-keys-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Dry Tortugas possible on a cruise day?</summary>
        <p class="mt-4 text-sm text-gray-500">Only on longer port calls (8+ hours). The ferry is a full-day commitment — verify your ship's departure before booking.</p></details>
      {_internal_links()}
    </div></section>"""


def _faq_schema() -> dict:
    qa = [
        ("How long do cruise ships stay in Key West?", "Most Key West calls are 6 to 10 hours."),
        ("Can you walk from the Key West cruise port?", "Yes — Duval Street is 5–15 minutes on foot from the main pier."),
        ("Do I need a tour or can I explore on my own?", "Many passengers walk Old Town independently; tours help when time is short."),
        ("What are the must-see sights?", "Southernmost Point, Duval Street, Hemingway House and Mallory Square."),
        ("Ship excursion or book independently?", "Ship tours guarantee wait-if-late; reputable locals plan buffer returns."),
        ("Is Dry Tortugas possible on a cruise day?", "Only on 8+ hour port calls due to ferry travel time."),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def main() -> None:
    print("Building Key West Shore Excursions site…")

    write(
        "partials/nav.html",
        f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-keys-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Key West<br/><span class="text-[10px] font-body font-normal text-keys-600 tracking-widest uppercase">Shore Excursions</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-key-west-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="can-you-walk-key-west-from-cruise-port.html" data-nav="walk" class="text-gray-600 hover:text-ocean-600 transition-colors">Walk</a>
        <a href="southernmost-point-tours.html" data-nav="sights" class="text-gray-600 hover:text-ocean-600 transition-colors">Sights</a>
        <a href="key-west-conch-train-tours.html" data-nav="tours" class="text-gray-600 hover:text-ocean-600 transition-colors">Tours</a>
        <a href="key-west-snorkelling-tours.html" data-nav="water" class="text-gray-600 hover:text-ocean-600 transition-colors">Water</a>
        <a href="key-west-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-key-west-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )

    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Key West from the walkable Florida Keys port. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-key-west-shore-excursions.html" class="hover:text-white transition-colors">Best Excursions</a></li>
            <li><a href="key-west-conch-train-tours.html" class="hover:text-white transition-colors">Conch Train</a></li>
            <li><a href="key-west-trolley-tours.html" class="hover:text-white transition-colors">Trolley Tours</a></li>
            <li><a href="key-west-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="key-west-dolphin-watching-tours.html" class="hover:text-white transition-colors">Dolphin Watching</a></li>
            <li><a href="key-west-sunset-sailing.html" class="hover:text-white transition-colors">Sunset Sailing</a></li>
            <li><a href="dry-tortugas-excursions.html" class="hover:text-white transition-colors">Dry Tortugas</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="key-west-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="can-you-walk-key-west-from-cruise-port.html" class="hover:text-white transition-colors">Walk From Port</a></li>
            <li><a href="one-day-in-key-west.html" class="hover:text-white transition-colors">One Day in Key West</a></li>
            <li><a href="southernmost-point-tours.html" class="hover:text-white transition-colors">Southernmost Point</a></li>
            <li><a href="duval-street-guide.html" class="hover:text-white transition-colors">Duval Street</a></li>
            <li><a href="hemingway-house-tours.html" class="hover:text-white transition-colors">Hemingway House</a></li>
            <li><a href="key-west-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="key-west-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
""",
    )

    write(
        "partials/trust-strip.html",
        f"""<section class="trust-strip" aria-label="Key West shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Walkable Old Town</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Southernmost Point</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Duval Street</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>
""",
    )

    heroes = {
        "hero-home.html": _hero_home(),
        "hero-excursions.html": _hero_inner(
            "Key West Cruise Port · Florida Keys",
            f"Best Key West<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare walkable Old Town, Southernmost Point, Conch Train, snorkelling, dolphin watching, sunset sailing and Dry Tortugas for your ship schedule.",
            BEST_IMG,
            BEST_ALT,
            breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            f"Key West<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Mallory Square and Outer Mole piers, walkable Old Town, USD currency and how to plan shore time ashore.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Port Guide",
            cta=("best-key-west-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 Walkable Port", "🏛️ Old Town", "📍 Southernmost Point", "🚂 Conch Train"],
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">Key West</span>",
            "Hour-by-hour plan from gangway to departure — Old Town walk, Conch Train or snorkel with return buffer.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="One Day in Key West",
        ),
        "hero-walk.html": _hero_inner(
            "Walkable Cruise Port",
            f"Can You Walk Key West<br/><span class=\"{ACCENT}\">From the Cruise Port?</span>",
            "Duval Street, Mallory Square and Old Town are minutes on foot — Southernmost Point is a longer flat walk.",
            WALK_IMG,
            WALK_ALT,
            breadcrumb="Walk From Port",
        ),
        "hero-southernmost.html": _hero_inner(
            "Landmark · Key West",
            f"Southernmost Point<br/><span class=\"{ACCENT}\">Tours</span>",
            "The famous buoy at the southernmost spot in the continental US — walk, ride or tour.",
            SOUTH_IMG,
            SOUTH_ALT,
            breadcrumb="Southernmost Point",
        ),
        "hero-duval.html": _hero_inner(
            "Old Town · Key West",
            f"Duval Street<br/><span class=\"{ACCENT}\">Guide</span>",
            "Shops, bars, galleries and key lime pie on Key West's colourful main strip.",
            DUVAL_IMG,
            DUVAL_ALT,
            breadcrumb="Duval Street",
        ),
        "hero-hemingway.html": _hero_inner(
            "Historic Home · Old Town",
            f"Hemingway House<br/><span class=\"{ACCENT}\">Tours</span>",
            "Ernest Hemingway's estate, six-toed cats and lush gardens in walkable Old Town.",
            HEMINGWAY_IMG,
            HEMINGWAY_ALT,
            breadcrumb="Hemingway House",
        ),
        "hero-conch.html": _hero_inner(
            "Sightseeing · Key West",
            f"Key West Conch<br/><span class=\"{ACCENT}\">Train Tours</span>",
            "Open-air train covering Old Town highlights with live narration since 1958.",
            CONCH_IMG,
            CONCH_ALT,
            breadcrumb="Conch Train",
        ),
        "hero-trolley.html": _hero_inner(
            "Hop-On Hop-Off · Key West",
            f"Key West<br/><span class=\"{ACCENT}\">Trolley Tours</span>",
            "Colourful trolley loops through Old Town with guided commentary and flexible stops.",
            TROLLEY_IMG,
            TROLLEY_ALT,
            breadcrumb="Trolley Tours",
        ),
        "hero-snorkelling.html": _hero_inner(
            "Florida Keys Reef · Key West",
            f"Key West<br/><span class=\"{ACCENT}\">Snorkelling</span> Tours",
            "Reef patches and clear water — catamaran trips with gear from the harbour.",
            SNORKEL_IMG,
            SNORKEL_ALT,
            breadcrumb="Snorkelling Tours",
        ),
        "hero-dolphin.html": _hero_inner(
            "Wildlife · Key West Harbour",
            f"Key West Dolphin<br/><span class=\"{ACCENT}\">Watching Tours</span>",
            "Wild Atlantic bottlenose dolphins on harbour boat trips with coastal scenery.",
            DOLPHIN_IMG,
            DOLPHIN_ALT,
            breadcrumb="Dolphin Watching",
        ),
        "hero-sunset.html": _hero_inner(
            "Golden Hour · Key West",
            f"Key West<br/><span class=\"{ACCENT}\">Sunset Sailing</span>",
            "Schooners and catamarans for harbour sunset views — classic Key West evening.",
            SUNSET_IMG,
            SUNSET_ALT,
            breadcrumb="Sunset Sailing",
        ),
        "hero-tortugas.html": _hero_inner(
            "National Park · 70 Miles West",
            f"Dry Tortugas<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Fort Jefferson day trips by ferry or seaplane — for longer port calls only.",
            TORTUGAS_IMG,
            TORTUGAS_ALT,
            breadcrumb="Dry Tortugas",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            f"Key West<br/><span class=\"{ACCENT}\">Family</span> Excursions",
            "Conch Train, walkable Old Town, dolphin watching and gentle snorkel trips for every generation.",
            FAMILY_IMG,
            FAMILY_ALT,
            breadcrumb="Family Excursions",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            f"Key West<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Port hours, walking from the pier, tours vs independent exploring and return-to-ship tips.",
            FAQ_IMG,
            FAQ_ALT,
            breadcrumb="FAQ",
        ),
    }
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = {
        "home.html": _content_home(),
        "best-key-west-shore-excursions.html": _content_best(),
        "key-west-cruise-port-guide.html": _content_port(),
        "one-day-in-key-west.html": _content_one_day(),
        "can-you-walk-key-west-from-cruise-port.html": _content_walk(),
        "southernmost-point-tours.html": _content_southernmost(),
        "duval-street-guide.html": _content_duval(),
        "hemingway-house-tours.html": _content_hemingway(),
        "key-west-conch-train-tours.html": _content_conch(),
        "key-west-trolley-tours.html": _content_trolley(),
        "key-west-snorkelling-tours.html": _content_snorkelling(),
        "key-west-dolphin-watching-tours.html": _content_dolphin(),
        "key-west-sunset-sailing.html": _content_sunset(),
        "dry-tortugas-excursions.html": _content_tortugas(),
        "key-west-family-excursions.html": _content_family(),
        "key-west-faq.html": _content_faq(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Walkable Old Town, Southernmost Point &amp; Conch Train",
            description="Plan Key West shore excursions for cruise passengers — walkable Old Town, Southernmost Point, Duval Street, Conch Train, snorkelling, dolphin watching and sunset sailing from the cruise port.",
            keywords="Key West shore excursions, Key West cruise excursions, walkable Key West cruise port, Southernmost Point tour, Conch Train Key West",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for Key West cruise shore excursions from the walkable Florida Keys port",
            },
        ),
        dict(
            file="best-key-west-shore-excursions.html",
            title="Best Key West Shore Excursions | Compare Walkable &amp; Guided Tours",
            description="Compare the best Key West shore excursions — walkable Old Town, Southernmost Point, Conch Train, snorkelling, dolphin watching, sunset sailing and Dry Tortugas with cruise timing.",
            keywords="best Key West shore excursions, Key West cruise port tours, compare Key West excursions, Conch Train cruise tour",
            path="best-key-west-shore-excursions.html",
            data_page="excursions",
            hero="partials/hero-excursions.html",
            content="best-key-west-shore-excursions.html",
            preload=BEST_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": "Best Key West Shore Excursions",
                "url": f"{DOMAIN}/best-key-west-shore-excursions.html",
            },
        ),
        dict(
            file="key-west-cruise-port-guide.html",
            title="Key West Cruise Port Guide | Walkable Mallory Square Pier",
            description="Key West cruise port guide — Mallory Square and Outer Mole piers, walkable Old Town, USD currency and top shore excursions timed for your ship's schedule.",
            keywords="Key West cruise port guide, Key West Mallory Square pier, Key West port day, cruise passenger guide Florida Keys",
            path="key-west-cruise-port-guide.html",
            data_page="port",
            hero="partials/hero-port-guide.html",
            content="key-west-cruise-port-guide.html",
            preload=PORT_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": "Key West Cruise Port Guide",
                "url": f"{DOMAIN}/key-west-cruise-port-guide.html",
            },
        ),
        dict(
            file="one-day-in-key-west.html",
            title="One Day in Key West from a Cruise Ship | Port Itinerary",
            description="How to spend one day in Key West on a cruise stop — Old Town walk, Southernmost Point, Conch Train and snorkel sample timeline with return-to-ship buffer.",
            keywords="one day in Key West cruise, Key West port day itinerary, walkable Key West cruise stop planning",
            path="one-day-in-key-west.html",
            data_page="port",
            hero="partials/hero-one-day.html",
            content="one-day-in-key-west.html",
            preload=ONE_DAY_IMG,
        ),
        dict(
            file="can-you-walk-key-west-from-cruise-port.html",
            title="Can You Walk Key West From the Cruise Port? | Port Guide",
            description="Yes — Key West is walkable from the cruise port. Duval Street and Mallory Square are minutes on foot; Southernmost Point is 1.5 miles. Tips for cruise passengers.",
            keywords="walk Key West from cruise port, walkable Key West cruise port, Key West Old Town walking distance",
            path="can-you-walk-key-west-from-cruise-port.html",
            data_page="walk",
            hero="partials/hero-walk.html",
            content="can-you-walk-key-west-from-cruise-port.html",
            preload=WALK_IMG,
        ),
        dict(
            file="southernmost-point-tours.html",
            title="Southernmost Point Tours | Key West Cruise Shore Excursions",
            description="Southernmost Point buoy tours from Key West cruise port — walk, pedicab or Conch Train to the famous continental US landmark.",
            keywords="Southernmost Point tour Key West, Southernmost Point buoy cruise, Key West landmark excursion",
            path="southernmost-point-tours.html",
            data_page="sights",
            hero="partials/hero-southernmost.html",
            content="southernmost-point-tours.html",
            preload=SOUTH_IMG,
        ),
        dict(
            file="duval-street-guide.html",
            title="Duval Street Guide | Key West Cruise Port Walking Guide",
            description="Duval Street guide for cruise passengers — shops, bars, key lime pie and colourful Old Town buildings minutes from the Key West cruise port.",
            keywords="Duval Street Key West cruise, Duval Street guide cruise port, Key West Old Town walking",
            path="duval-street-guide.html",
            data_page="sights",
            hero="partials/hero-duval.html",
            content="duval-street-guide.html",
            preload=DUVAL_IMG,
        ),
        dict(
            file="hemingway-house-tours.html",
            title="Hemingway House Tours | Key West Cruise Shore Excursions",
            description="Ernest Hemingway Home tours for cruise passengers — six-toed cats, historic estate and gardens in walkable Old Town Key West.",
            keywords="Hemingway House tour Key West cruise, Ernest Hemingway Home excursion, Key West literary tour",
            path="hemingway-house-tours.html",
            data_page="sights",
            hero="partials/hero-hemingway.html",
            content="hemingway-house-tours.html",
            preload=HEMINGWAY_IMG,
        ),
        dict(
            file="key-west-conch-train-tours.html",
            title="Key West Conch Train Tours | Old Town Sightseeing",
            description="Key West Conch Train tours from the cruise port — 90-minute open-air sightseeing loop through Old Town with live narration.",
            keywords="Key West Conch Train cruise, Conch Tour Train shore excursion, Old Town sightseeing Key West",
            path="key-west-conch-train-tours.html",
            data_page="tours",
            hero="partials/hero-conch.html",
            content="key-west-conch-train-tours.html",
            preload=CONCH_IMG,
        ),
        dict(
            file="key-west-trolley-tours.html",
            title="Key West Trolley Tours | Hop-On Hop-Off Cruise Excursions",
            description="Key West trolley tours for cruise passengers — hop-on hop-off Old Town sightseeing with guided commentary from the harbour.",
            keywords="Key West trolley tour cruise, hop on hop off Key West, Old Town trolley shore excursion",
            path="key-west-trolley-tours.html",
            data_page="tours",
            hero="partials/hero-trolley.html",
            content="key-west-trolley-tours.html",
            preload=TROLLEY_IMG,
        ),
        dict(
            file="key-west-snorkelling-tours.html",
            title="Key West Snorkelling Tours | Reef Cruise Excursions",
            description="Key West snorkelling tours from the cruise port — Florida Keys reef patches, catamaran trips and cruise-friendly returns.",
            keywords="Key West snorkelling tour cruise, reef snorkel Key West, snorkel shore excursion Florida Keys",
            path="key-west-snorkelling-tours.html",
            data_page="water",
            hero="partials/hero-snorkelling.html",
            content="key-west-snorkelling-tours.html",
            preload=SNORKEL_IMG,
        ),
        dict(
            file="key-west-dolphin-watching-tours.html",
            title="Key West Dolphin Watching Tours | Cruise Shore Excursions",
            description="Key West dolphin watching tours for cruise passengers — wild bottlenose dolphins on harbour boat trips with cruise-friendly returns.",
            keywords="Key West dolphin watching cruise, dolphin tour Key West port, wildlife excursion Florida Keys",
            path="key-west-dolphin-watching-tours.html",
            data_page="water",
            hero="partials/hero-dolphin.html",
            content="key-west-dolphin-watching-tours.html",
            preload=DOLPHIN_IMG,
        ),
        dict(
            file="key-west-sunset-sailing.html",
            title="Key West Sunset Sailing | Cruise Port Evening Excursions",
            description="Key West sunset sailing excursions — schooners and catamarans for golden-hour harbour views on late-departure cruise days.",
            keywords="Key West sunset sailing cruise, sunset sail Key West port, evening excursion Florida Keys",
            path="key-west-sunset-sailing.html",
            data_page="water",
            hero="partials/hero-sunset.html",
            content="key-west-sunset-sailing.html",
            preload=SUNSET_IMG,
        ),
        dict(
            file="dry-tortugas-excursions.html",
            title="Dry Tortugas Excursions | Fort Jefferson Day Trips from Key West",
            description="Dry Tortugas and Fort Jefferson excursions from Key West — ferry and seaplane day trips for cruise passengers on long port calls.",
            keywords="Dry Tortugas excursion Key West cruise, Fort Jefferson day trip, Yankee Freedom cruise port",
            path="dry-tortugas-excursions.html",
            data_page="water",
            hero="partials/hero-tortugas.html",
            content="dry-tortugas-excursions.html",
            preload=TORTUGAS_IMG,
        ),
        dict(
            file="key-west-family-excursions.html",
            title="Key West Family Excursions | Kid-Friendly Cruise Tours",
            description="Family-friendly Key West excursions — Conch Train, walkable Old Town, dolphin watching and snorkelling for cruise guests with children.",
            keywords="Key West family excursions, kid friendly Key West cruise tours, family shore excursion Florida Keys",
            path="key-west-family-excursions.html",
            data_page="family",
            hero="partials/hero-family.html",
            content="key-west-family-excursions.html",
            preload=FAMILY_IMG,
        ),
        dict(
            file="key-west-faq.html",
            title="Key West Shore Excursions FAQ | Cruise Port Planning",
            description="FAQ for Key West shore excursions — walkable port, port hours, tours vs independent exploring, must-see sights and return-to-ship tips.",
            keywords="Key West shore excursions FAQ, Key West cruise port questions, walkable port FAQ",
            path="key-west-faq.html",
            data_page="port",
            hero="partials/hero-faq.html",
            content="key-west-faq.html",
            preload=FAQ_IMG,
            schema=_faq_schema(),
        ),
    ]

    for p in pages:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-key-west-shore-excursions.html", "0.9", "monthly"),
        ("key-west-cruise-port-guide.html", "0.8", "monthly"),
        ("can-you-walk-key-west-from-cruise-port.html", "0.9", "monthly"),
        ("one-day-in-key-west.html", "0.8", "monthly"),
        ("southernmost-point-tours.html", "0.9", "monthly"),
        ("duval-street-guide.html", "0.8", "monthly"),
        ("hemingway-house-tours.html", "0.8", "monthly"),
        ("key-west-conch-train-tours.html", "0.9", "monthly"),
        ("key-west-trolley-tours.html", "0.8", "monthly"),
        ("key-west-snorkelling-tours.html", "0.9", "monthly"),
        ("key-west-dolphin-watching-tours.html", "0.8", "monthly"),
        ("key-west-sunset-sailing.html", "0.8", "monthly"),
        ("dry-tortugas-excursions.html", "0.8", "monthly"),
        ("key-west-family-excursions.html", "0.8", "monthly"),
        ("key-west-faq.html", "0.7", "monthly"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in urls:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write(
        "package.json",
        """{
  "name": "key-west-shore-excursions",
  "private": true,
  "scripts": {
    "build": "python3 scripts/build-key-west-site.py",
    "images": "python3 scripts/fetch-key-west-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8912"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""",
    )

    write(
        "wrangler.jsonc",
        """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "key-west-shore-excursions",
  "compatibility_date": "2026-06-06",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "keywestshoreexcursions.com",
      "custom_domain": true
    }
  ]
}
""",
    )

    write(
        "deploy.sh",
        f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""",
    )

    (ROOT / "deploy.sh").chmod(0o755)

    write(
        "images/ATTRIBUTION.md",
        """# Image attribution

Hero and content images may be sourced from Unsplash (Unsplash License) via `npm run images`.

Replace placeholder images with your own Key West photography where noted in `scripts/fetch-key-west-images.py` (`CUSTOM_IMAGES`).
""",
    )

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    placeholders = [
        HOME_HERO,
        BEST_IMG,
        PORT_IMG,
        ONE_DAY_IMG,
        WALK_IMG,
        SOUTH_IMG,
        DUVAL_IMG,
        HEMINGWAY_IMG,
        CONCH_IMG,
        TROLLEY_IMG,
        SNORKEL_IMG,
        DOLPHIN_IMG,
        SUNSET_IMG,
        TORTUGAS_IMG,
        FAMILY_IMG,
        FAQ_IMG,
        INTRO_IMG,
    ]
    for img in placeholders:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        if not p.exists() or p.stat().st_size <= 5000:
            p.write_bytes(
                b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
                b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
                b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
                b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
            )

    print("Done.")


if __name__ == "__main__":
    main()
