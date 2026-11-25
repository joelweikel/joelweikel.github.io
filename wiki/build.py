"""Build the static MMORP Wiki from content.py. No third-party packages required."""
from collections import Counter
from html import escape
from pathlib import Path
import json
import re
import sys

sys.dont_write_bytecode = True
from content import ARTICLES, CATEGORIES

ROOT = Path(__file__).resolve().parent
BY_SLUG = {item["slug"]: item for item in ARTICLES}
COUNTS = Counter(item["category"] for item in ARTICLES)

def e(value):
    return escape(str(value), quote=True)

def inline(value):
    """Render [[slug|label]] links and escape all other text."""
    result, cursor = [], 0
    for match in re.finditer(r"\[\[([a-z0-9-]+)\|([^\]]+)\]\]", str(value)):
        result.append(e(str(value)[cursor:match.start()]))
        slug, label = match.groups()
        if slug not in BY_SLUG:
            raise ValueError(f"Unknown article: {slug}")
        result.append(f'<a href="{e(slug)}.html">{e(label)}</a>')
        cursor = match.end()
    result.append(e(str(value)[cursor:]))
    return "".join(result)

def section_id(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

def asset(filename):
    if not (ROOT / "assets" / filename).is_file():
        raise FileNotFoundError(filename)
    return "assets/" + e(filename)

def image(filename, alt, css="", lazy=True):
    loading = ' loading="lazy"' if lazy else ''
    return f'<img class="{css}" src="{asset(filename)}" alt="{e(alt)}"{loading} decoding="async">'

def site_header():
    return '''<div id="header-placeholder">
        <header>
            <div class="container header-inner">
                <a class="site-title" href="../index.html">Joel Weikel<span class="title-dot">.</span></a>
                <button class="menu-toggle" id="menuToggle" aria-expanded="false" aria-controls="mainNav">Menu <span aria-hidden="true">+</span></button>
                <nav id="mainNav" aria-label="Main navigation">
                    <ul>
                        <li><a href="../index.html">About</a></li>
                        <li><a href="../janthina-drone.html">Drone</a></li>
                        <li><a href="../metals.html">Foundry</a></li>
                        <li><a href="../games.html">Games</a></li>
                        <li><a href="../projects.html">More projects</a></li>
                        <li><a href="../Resume.pdf">Résumé ↗</a></li>
                    </ul>
                </nav>
            </div>
        </header>
    </div>'''

def wiki_bar():
    return '''<div class="wiki-bar">
        <div class="container wiki-bar-inner">
            <a class="wiki-wordmark" href="index.html" aria-label="MMORP Wiki home"><span>MMORP</span><small>THE WIKI</small></a>
            <nav class="wiki-topnav" aria-label="Wiki navigation">
                <a href="index.html#characters">Characters</a>
                <a href="index.html#games">Games</a>
                <a href="index.html#world">World</a>
                <a href="index.html#joeltech">Joeltech</a>
            </nav>
            <div class="wiki-search">
                <form id="wiki-search-form" role="search" action="index.html#browse">
                    <label class="sr-only" for="wiki-search-input">Search the MMORP Wiki</label>
                    <span class="search-icon" aria-hidden="true"></span>
                    <input id="wiki-search-input" type="search" placeholder="Search the wiki" autocomplete="off" aria-controls="search-results" aria-describedby="search-help">
                    <button type="submit" class="search-submit">Search</button>
                </form>
                <div class="search-results" id="search-results" hidden></div>
                <span class="sr-only" id="search-help">Search articles by name or keyword. Results appear below the search field.</span>
                <span class="sr-only" id="search-announcement" role="status" aria-live="polite"></span>
            </div>
        </div>
    </div>'''

def frame(title, description, body, active=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#0a3d62">
<title>{e(title)} | MMORP Wiki</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,500;0,600;1,400&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
<link rel="stylesheet" href="wiki.css">
<script src="search-data.js" defer></script>
<script src="wiki.js" defer></script>
<noscript><style>@media(max-width:700px){{header nav{{display:block;position:static}}header nav ul{{display:flex;flex-wrap:wrap;gap:5px 20px;padding:0 0 20px}}header nav a{{font-size:12px}}.header-inner{{flex-wrap:wrap;padding-top:15px}}.menu-toggle{{display:none}}}}</style></noscript>
</head>
<body class="wiki-page" id="top">
<a class="skip-link" href="#main">Skip to content</a>
{site_header()}
{wiki_bar()}
{body}
<footer class="wiki-footer">
    <div class="container wiki-footer-inner">
        <div><a class="footer-brand" href="index.html">MMORP <span>WIKI</span></a><p>A little corner of the MMORP universe.</p></div>
        <div class="footer-links"><a href="../games.html">More games</a><a href="../index.html">Joel Weikel</a><a href="#top">Back to top</a></div>
    </div>
</footer>
</body>
</html>
'''

def sidebar():
    category_links = "".join(
        f'<li><a href="index.html#{slug}">{e(name)} <span>{COUNTS[slug]}</span></a></li>'
        for slug, (name, _) in CATEGORIES.items()
    )
    return f'''<aside class="wiki-sidebar" aria-label="Explore the wiki">
        <p class="rail-heading">The MMORP Wiki</p>
        <a class="rail-home" href="index.html">Wiki home</a>
        <p class="rail-heading">Explore</p>
        <ul>{category_links}</ul>
        <div class="rail-note"><span>THE ORIGINAL</span><p>Ten levels. A lot of projectiles.</p><a href="mmorp-1.html">Explore MMORP</a></div>
    </aside>'''

def article_card(item):
    return f'''<a class="entry-card" href="{e(item["slug"])}.html">
        <span class="entry-image {"is-art" if item["art"] else ""}">{image(item["image"], "", lazy=True)}</span>
        <span class="entry-copy"><strong>{e(item["title"])}</strong><span>{e(item["summary"])}</span></span>
    </a>'''

GAME_ENEMIES = {
        "mmorp-1": [
            ("squelch", "squelch-classic.svg"), ("plopper", "plopper-classic.svg"),
            ("threnemy", "threnemy-classic.svg"), ("helper", "helper-classic.svg"),
            ("chomper", "chomper-open.svg"), ("wall", "wall.svg"), ("momo", "momo.svg"),
            ("prickly", "prickly.svg"), ("derek", "derek.svg"), ("tennemy", "tennemy.svg"),
        ],
        "mmorp-3d": [
            ("squelch", "squelch.webp"), ("plopper", "plopper.webp"),
            ("threnemy", "threnemy.webp"), ("helper", "helper.webp"),
            ("chomper", "chomper.webp"), ("gulper", "gulper.webp"),
            ("toother", "toother.webp"), ("spiker", "spiker.webp"),
        ],
}

def home():
    categories = []
    for slug, (name, desc) in CATEGORIES.items():
        cards = "".join(article_card(item) for item in ARTICLES if item["category"] == slug)
        categories.append(f'''<section class="browse-group" id="{slug}" data-group="{slug}">
            <div class="group-heading"><div><p class="section-kicker">EXPLORE THE WIKI</p><h3>{e(name)}</h3><p>{e(desc)}</p></div><span>{COUNTS[slug]} articles</span></div>
            <div class="entry-grid">{cards}</div>
        </section>''')
    level_links = "".join(f'<li><a href="{slug}.html"><span>{n:02}</span>{e(BY_SLUG[slug]["title"])}</a></li>' for n, (slug, _) in enumerate(GAME_ENEMIES["mmorp-1"], 1))
    filters = '<button type="button" data-filter="all" aria-pressed="true">All articles</button>' + "".join(
        f'<button type="button" data-filter="{slug}" aria-pressed="false">{e(name)}</button>'
        for slug, (name, _) in CATEGORIES.items()
    )
    portal_data = [
        ("characters", "Characters", "Meet the cast", "plopper.webp"),
        ("games", "Games & mechanics", "Play through the series", "mmorp1-splash.webp"),
        ("world", "World & lore", "See the sights", "archipelago.webp"),
        ("joeltech", "Joeltech", "Think higher", "gale.webp"),
    ]
    portals = "".join(f'''<a class="portal portal-{slug}" href="#{slug}">
        <span class="portal-art">{image(img, "")}</span>
        <span class="portal-label"><small>{e(tagline)}</small><strong>{e(label)}</strong><span>{COUNTS[slug]} articles</span></span>
    </a>''' for slug, label, tagline, img in portal_data)
    return f'''<main id="main">
    <section class="wiki-cover">
        <div class="container cover-grid">
            <div class="cover-copy">
                <p class="cover-kicker"><span></span> AN EVER-EXPANDING UNIVERSE</p>
                <h1>The world<br>of <em>MMORP.</em></h1>
                <p>One character. A lot of enemies. An entire universe of games, places, and wonderfully questionable lore.</p>
                <div class="cover-actions"><a class="cover-button" href="#browse">Explore the wiki</a><a class="cover-link" href="mmorp.html">Meet MMORP</a></div>
            </div>
            <div class="cover-visual" aria-hidden="true">
                <div class="cover-orbit orbit-one"></div><div class="cover-orbit orbit-two"></div>
                <span class="cover-spark spark-one">✦</span><span class="cover-spark spark-two">✳</span>
                {image("mmorp.webp", "", "cover-character", lazy=False)}
                <div class="cover-stamp">THE<br>MMORP<br>UNIVERSE</div>
            </div>
        </div>
        <div class="container cover-bottom"><span>GAMES · CHARACTERS · LORE</span><span>EST. IN SCRATCH, 2021</span></div>
    </section>
    <div class="container wiki-layout home-layout">
        {sidebar()}
        <div class="wiki-content">
            <section class="welcome-section">
                <div><p class="section-kicker">WELCOME TO THE ARCHIVE</p><h2>There’s more to<br><em>the story.</em></h2></div>
                <div><p>What started as a Scratch game became a world of its own. Get to know the characters, revisit the games, and see where the lore goes.</p><p class="welcome-count"><strong>{len(ARTICLES)}</strong> articles to explore <span>·</span> one very unusual universe</p></div>
            </section>
            <section class="portals-section" aria-labelledby="portals-title">
                <div class="section-heading-inline"><div><p class="section-kicker">PICK A STARTING POINT</p><h2 id="portals-title">Explore by category</h2></div></div>
                <div class="portal-grid">{portals}</div>
            </section>
            <section class="feature-section">
                <div class="feature-copy"><p class="section-kicker">FROM THE ARCHIVE</p><h2>Meet the<br><em>Threnemy.</em></h2><p>A spinning wheel. Waves of three. The third level of the original MMORP has a way of making an entrance.</p><a href="threnemy.html">Read the article</a></div>
                <div class="feature-art">{image("threnemy-wheel.webp", "The Threnemy spawner wheel in MMORP 3D")}</div>
            </section>
            <section class="level-section">
                <div class="section-heading-inline"><div><p class="section-kicker">THE ORIGINAL GAME</p><h2>Meet the classic ten</h2><p>From the first Squelch to the infamous Tennemy.</p></div><a class="subtle-link" href="mmorp-1.html">About the game</a></div>
                <ol class="level-list">{level_links}</ol>
            </section>
            <section class="browse-section" id="browse">
                <div class="browse-intro"><div><p class="section-kicker">THE ENCYCLOPEDIA</p><h2>All articles</h2></div><p>Browse the archive or use the search above to find something specific.</p></div>
                <div class="filter-bar" aria-label="Filter articles by category" hidden>{filters}</div>
                <p class="sr-only" id="filter-announcement" role="status" aria-live="polite"></p>
                {"".join(categories)}
            </section>
        </div>
    </div>
    </main>'''

def infobox(item):
    rows = "".join(f'<div><dt>{e(name)}</dt><dd>{inline(value)}</dd></div>' for name, value in item["facts"])
    return f'''<aside class="infobox" aria-label="{e(item["title"])} facts">
        <h2>{e(item["title"])}</h2>
        <div class="infobox-image {"is-art" if item["art"] else ""}">{image(item["image"], item["alt"], lazy=False)}</div>
        <p class="infobox-caption">{e(CATEGORIES[item["category"]][0])}</p>
        <dl>{rows}</dl>
    </aside>'''

def article_page(item):
    sections = []
    for section in item["sections"]:
        paragraphs = "".join(f'<p>{inline(paragraph)}</p>' for paragraph in section["paragraphs"])
        bullets = "".join(f'<li>{inline(bullet)}</li>' for bullet in section["bullets"])
        if bullets:
            paragraphs += f"<ul>{bullets}</ul>"
        sections.append(f'<section class="article-section" id="{section_id(section["title"])}"><h2>{e(section["title"])}</h2>{paragraphs}</section>')
    toc_links = "".join(f'<li><a href="#{section_id(section["title"])}">{e(section["title"])}</a></li>' for section in item["sections"])
    if item["slug"] in GAME_ENEMIES:
        toc_links += '<li><a href="#enemies">Enemies</a></li>'
        cards = "".join(article_card({**BY_SLUG[slug], "image": filename, "art": True}) for slug, filename in GAME_ENEMIES[item["slug"]])
        sections.append(f'<section class="article-section" id="enemies"><h2>Enemies</h2><div class="entry-grid">{cards}</div></section>')
    if item["gallery"]:
        toc_links += '<li><a href="#gallery">Gallery</a></li>'
        figures = "".join(f'''<figure><a href="{asset(filename)}" target="_blank" rel="noopener" aria-label="Open image: {e(caption)}">{image(filename, caption)}</a><figcaption>{e(caption)}</figcaption></figure>''' for filename, caption in item["gallery"])
        sections.append(f'<section class="article-section article-gallery" id="gallery"><h2>Gallery</h2><div class="gallery-grid">{figures}</div></section>')
    if item["video"]:
        filename, poster, caption = item["video"]
        toc_links += '<li><a href="#video">Video</a></li>'
        sections.append(f'<section class="article-section article-video" id="video"><h2>Video</h2><figure><video controls preload="none" playsinline poster="{asset(poster)}"><source src="{asset(filename)}" type="video/mp4">Your browser does not support video. <a href="{asset(filename)}">Download the video</a>.</video><figcaption>{e(caption)}</figcaption></figure></section>')
    action_links = "".join(f'<a class="article-action" href="{e(url)}"{" target=\"_blank\" rel=\"noopener noreferrer\"" if url.startswith("https://") else ""}>{e(label)}</a>' for label, url in item["links"])
    if action_links:
        sections.append(f'<div class="article-actions">{action_links}</div>')
    related = [BY_SLUG[slug] for slug in item["related"]]
    related_html = ""
    if related:
        cards = "".join(article_card(other) for other in related)
        related_html = f'<section class="related-section"><p class="section-kicker">KEEP EXPLORING</p><h2>Related articles</h2><div class="entry-grid">{cards}</div></section>'
    name = CATEGORIES[item["category"]][0]
    return f'''<main id="main" class="article-page">
    <div class="container wiki-layout">
        {sidebar()}
        <div class="wiki-content article-content">
            <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">MMORP Wiki</a><span>/</span><a href="index.html#{e(item["category"])}">{e(name)}</a><span>/</span><span aria-current="page">{e(item["title"])}</span></nav>
            <div class="article-heading"><p class="section-kicker">{e(name)}</p><h1>{e(item["title"])}</h1><p class="article-lead">{e(item["summary"])}</p></div>
            <div class="article-grid">
                <div class="article-copy">
                    <nav class="toc" aria-label="Contents"><h2>On this page</h2><ol>{toc_links}</ol></nav>
                    {"".join(sections)}
                </div>
                {infobox(item)}
            </div>
            {related_html}
        </div>
    </div>
    </main>'''

def main():
    if len(BY_SLUG) != len(ARTICLES):
        raise ValueError("Article slugs must be unique")
    for item in ARTICLES:
        if item["category"] not in CATEGORIES:
            raise ValueError(f'Unknown category: {item["category"]}')
        for slug in item["related"]:
            if slug not in BY_SLUG:
                raise ValueError(f'Unknown related article: {slug}')
    (ROOT / "index.html").write_text(frame("Home", "Explore the characters, games, places, and lore of the MMORP universe.", home()), encoding="utf-8")
    for item in ARTICLES:
        (ROOT / (item["slug"] + ".html")).write_text(frame(item["title"], item["summary"], article_page(item)), encoding="utf-8")
    search = []
    for item in ARTICLES:
        body = " ".join(section["title"] + " " + " ".join(section["paragraphs"] + section["bullets"]) for section in item["sections"])
        body += " " + " ".join(name + " " + value for name, value in item["facts"])
        body = re.sub(r"\[\[([a-z0-9-]+)\|([^\]]+)\]\]", r"\2", body)
        search.append({"title": item["title"], "slug": item["slug"], "category": CATEGORIES[item["category"]][0],
                       "summary": item["summary"], "keywords": " ".join(item["aliases"]) + " " + body})
    (ROOT / "search-data.js").write_text("window.MMORP_SEARCH = " + json.dumps(search, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"Built {len(ARTICLES)} articles and the wiki home page.")

if __name__ == "__main__":
    main()
