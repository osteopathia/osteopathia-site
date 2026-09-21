"""Generate the ten static English/Russian foundation pages."""
from pathlib import Path
import posixpath

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "en": [("", "Home", ""), ("about", "About Me", "A short professional introduction will be added here."), ("approach", "My Approach", "A description of my approach will be added here."), ("articles", "Articles", "Articles and professional notes will be added here."), ("contact", "Contact", "Current contact details will be added here.")],
    "ru": [("", "Главная", ""), ("about", "Обо мне", "Здесь появится краткое профессиональное представление."), ("approach", "Мой подход", "Здесь появится описание моего подхода."), ("articles", "Статьи", "Здесь появятся статьи и профессиональные заметки."), ("useful", "Полезное", "Здесь появятся полезные материалы и рекомендации.")],
}
HERO = {"": "hero-home.webp", "about": "hero-about.webp", "approach": "hero-approach.webp", "articles": "hero-articles.webp", "contact": "hero-contact.webp", "useful": "hero-useful.webp"}
ICONS = {"about": "○", "approach": "≈", "articles": "≡", "contact": "→", "useful": "+"}

def folder(lang, slug):
    return "/".join(x for x in [("ru" if lang == "ru" else ""), slug] if x)

def render(lang, slug, title, text):
    ru = lang == "ru"
    current = folder(lang, slug)
    def link(target):
        relative = posixpath.relpath(target or ".", current or ".")
        return "./" if relative == "." else relative + "/"
    root = link("")
    home = link(folder(lang, ""))
    counterpart = slug if slug in ("about", "approach", "articles") else ""
    en = link(folder("en", slug if not ru else counterpart))
    rus = link(folder("ru", slug if ru else counterpart))
    nav = "".join(f'<a href="{link(folder(lang,s))}"' + (' aria-current="page"' if s == slug else '') + f'>{t}</a>' for s,t,_ in PAGES[lang][1:])
    name = "Роман Двулат" if ru else "Roman Dvulat, D.O."
    role = "Остеопат / Мануальный практик" if ru else "Osteopath / Manual Practitioner"
    welcome = "Личный профессиональный сайт" if ru else "Personal professional practice"
    intro = "Материалы готовятся." if ru else "Content is being prepared."
    image = f'{root}assets/images/{HERO[slug]}'
    header = f'''<header class="site-header"><div class="header-top wrap">
  <a class="brand" href="{home}"><span class="brand-name">Osteopathia<span>.ca</span></span><span class="brand-service">Canada U-Paramed Service</span></a>
  <div class="header-actions"><nav class="main-nav" aria-label="{'Основная навигация' if ru else 'Main navigation'}">{nav}</nav>
  <nav class="language" aria-label="{'Язык' if ru else 'Language'}"><a href="{en}" lang="en" hreflang="en" {'aria-current="true"' if not ru else ''}>EN</a><span>|</span><a href="{rus}" lang="ru" hreflang="ru" {'aria-current="true"' if ru else ''}>RU</a></nav></div>
</div></header>'''
    if not slug:
        cards = "".join(f'<a class="section-card" href="{link(folder(lang,s))}"><span class="card-icon" aria-hidden="true">{ICONS[s]}</span><strong>{t}</strong><span>{"Открыть раздел" if ru else "Explore section"} →</span></a>' for s,t,_ in PAGES[lang][1:])
        body = f'''<main id="main" tabindex="-1"><section class="hero"><img class="hero-media" src="{image}" alt="" width="1983" height="793"><div class="hero-inner"><div class="hero-copy"><p class="eyebrow">{welcome}</p><h1>{name}</h1><p class="profession">{role}</p><div class="short-rule"></div><p class="intro">{intro}</p><a class="button" href="{link(folder(lang,'about'))}">{'Обо мне' if ru else 'About Me'} <span aria-hidden="true">→</span></a></div></div></section><section class="home-sections wrap"><nav class="section-links" aria-label="{'Разделы сайта' if ru else 'Explore the website'}">{cards}</nav></section></main>'''
    else:
        body = f'''<main id="main" tabindex="-1"><section class="page-hero"><img class="hero-media" src="{image}" alt="" width="2000" height="800"><div class="page-hero-inner"><a class="back-link" href="{home}">← {'Главная' if ru else 'Home'}</a><p class="eyebrow">{name}</p><h1>{title}</h1><p class="profession">{role}</p></div></section><section class="page-body wrap"><div class="content-panel"><p>{text}</p></div></section></main>'''
    desc = f"{title} — Osteopathia.ca. " + ("Описание страницы будет добавлено." if ru else "Page description to be added.")
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name if not slug else title} | Osteopathia.ca</title>
  <meta name="description" content="{desc}">
  <link rel="preload" href="{image}" as="image" type="image/webp">
  <link rel="stylesheet" href="{root}assets/style.css">
  <link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
</head>
<body>
<a class="skip-link" href="#main">{'Перейти к содержанию' if ru else 'Skip to content'}</a>
{header}
{body}
<footer class="site-footer"><div class="wrap footer-inner"><span class="footer-brand">Osteopathia.ca</span><span class="footer-note"><span>Canada U-Paramed Service</span><span>© {name}</span></span></div></footer>
</body>
</html>
'''

for lang, pages in PAGES.items():
    for slug, title, text in pages:
        dest = ROOT / folder(lang, slug) / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(lang, slug, title, text), encoding="utf-8")
print("Generated 10 redesigned static pages.")
