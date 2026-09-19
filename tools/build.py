"""Optional authoring helper. Run python tools/build.py; hosting serves HTML only."""
from pathlib import Path
import posixpath
ROOT = Path(__file__).resolve().parents[1]
PAGES = {
'en': [('', 'Home', ''), ('about', 'About Me', 'A short professional introduction will be added here.'), ('approach', 'My Approach', 'A description of my approach will be added here.'), ('articles', 'Articles', 'Articles and professional notes will be added here.'), ('contact', 'Contact', 'Current contact details will be added here.')],
'ru': [('', 'Главная', ''), ('about', 'Обо мне', 'Здесь появится краткое профессиональное представление.'), ('approach', 'Мой подход', 'Здесь появится описание моего подхода.'), ('articles', 'Статьи', 'Здесь появятся статьи и профессиональные заметки.'), ('useful', 'Полезное', 'Здесь появятся полезные материалы и рекомендации.')]
}
def folder(lang, slug):
    return '/'.join(x for x in [('ru' if lang == 'ru' else ''), slug] if x)
def render(lang, slug, title, text):
    ru = lang == 'ru'
    current = folder(lang, slug)
    def link(target):
        relative = posixpath.relpath(target or '.', current or '.')
        return './' if relative == '.' else relative + '/'
    root = link('')
    home = link(folder(lang, ''))
    other = 'en' if ru else 'ru'
    counterpart = slug if slug in ('about', 'approach', 'articles') else ''
    en = link(folder('en', slug if lang == 'en' else counterpart))
    rus = link(folder('ru', slug if ru else counterpart))
    nav = ''.join(f'<a href="{link(folder(lang,s))}"' + (' aria-current="page"' if s==slug else '') + f'>{t}</a>' for s,t,_ in PAGES[lang][1:])
    name = 'Роман Двулат' if ru else 'Roman Dvulat, D.O.'
    role = 'Остеопат / Мануальный практик' if ru else 'Osteopath / Manual Practitioner'
    placeholder = 'МЕСТО ДЛЯ ФОТО' if ru else 'PHOTO PLACEHOLDER'
    caption = 'Новая профессиональная фотография появится здесь.' if ru else 'A new professional photograph will appear here.'
    coming = 'Материалы готовятся.' if ru else 'Content is being prepared.'
    welcome = 'Личный профессиональный сайт' if ru else 'Personal professional website'
    portrait = f'<figure class="portrait"><div class="photo-placeholder" role="img" aria-label="{caption}"><span class="photo-frame" aria-hidden="true"></span><strong>{placeholder}</strong></div><figcaption>{caption}</figcaption></figure>'
    if not slug:
        cards = ''.join(f'<a class="section-link" href="{link(folder(lang,s))}"><span>{t}</span><span aria-hidden="true">↗</span></a>' for s,t,_ in PAGES[lang][1:])
        body = f'<section class="hero"><div class="hero-copy"><p class="eyebrow">{welcome}</p><h1>{name}</h1><p class="profession">{role}</p><div class="short-rule"></div><p class="intro">{coming}</p><a class="text-link" href="{link(folder(lang,"about"))}">{"Обо мне" if ru else "About Me"} <span aria-hidden="true">→</span></a></div>{portrait}</section><nav class="section-links" aria-label="{"Разделы сайта" if ru else "Explore the website"}">{cards}</nav>'
    else:
        body = f'<div class="page-heading"><a class="back-link" href="{home}">← {"Главная" if ru else "Home"}</a><p class="eyebrow">{name}</p><h1>{title}</h1></div><section class="content-panel" aria-label="{title}"><p>{text}</p></section>'
    desc = f'{title} — Osteopathia.ca. ' + ('Описание страницы будет добавлено.' if ru else 'Page description to be added.')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{name if not slug else title} | Osteopathia.ca</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="{root}assets/style.css">
  <link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
</head>
<body>
<a class="skip-link" href="#main">{"Перейти к содержанию" if ru else "Skip to content"}</a>
<header class="site-header"><div class="header-top wrap">
  <a class="brand" href="{home}"><span class="brand-name">Osteopathia<span>.ca</span></span><span class="brand-service">Canada U-Paramed Service</span></a>
  <nav class="language" aria-label="{"Язык" if ru else "Language"}"><a href="{en}" lang="en" hreflang="en" {'aria-current="true"' if not ru else ''}>EN</a><span aria-hidden="true">|</span><a href="{rus}" lang="ru" hreflang="ru" {'aria-current="true"' if ru else ''}>RU</a></nav>
</div><nav class="main-nav wrap" aria-label="{"Основная навигация" if ru else "Main navigation"}">{nav}</nav></header>
<main id="main" class="wrap" tabindex="-1">{body}</main>
<footer class="site-footer"><div class="wrap footer-inner"><span>© {name}</span><span>Osteopathia.ca</span></div></footer>
</body>
</html>
'''
for lang,pages in PAGES.items():
    for slug,title,text in pages:
        dest = ROOT / folder(lang,slug) / 'index.html'
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(render(lang,slug,title,text),encoding='utf-8')
print('Generated 10 static pages.')
