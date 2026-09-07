import html
import xml.etree.ElementTree as ET
from pathlib import Path

base_dir = Path(__file__).resolve().parent
xml_path = base_dir / 'portfolio-content.xml'
html_path = base_dir / 'index.html'

CSS = """@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600;1,700&display=swap');
:root{ --paper:#fffaf0; --ink:#17213b; --muted:#667086; --blue:#254de8; --cyan:#57d9d0; --orange:#ff8a54; --yellow:#ffd34e; --coral:#ff6f91; --violet:#9c7cff; --dark:#17213b; --line:#d9d8d0; --white:#fff; }
*{box-sizing:border-box} html{scroll-behavior:smooth} body{margin:0;background:var(--paper);color:var(--ink);font-family:'DM Sans',sans-serif;line-height:1.65} a{color:inherit;text-decoration:none}
.wrap{width:min(calc(100% - 56px),1180px);margin:auto}
.top-stripe{height:7px;background:linear-gradient(90deg,var(--blue) 0 25%,var(--orange) 25% 50%,var(--cyan) 50% 75%,var(--yellow) 75%)}
.header{height:78px;border-bottom:1px solid var(--line);background:rgba(255,250,240,.9);backdrop-filter:blur(14px);position:sticky;top:0;z-index:100}.nav{height:100%;display:flex;align-items:center;justify-content:space-between}.logo{font:700 26px 'DM Sans';letter-spacing:-.06em}.logo span{color:var(--orange)}.navlinks{display:flex;gap:30px;font-size:12px;font-weight:700}.navlinks a{opacity:.65}.navlinks a:hover{opacity:1;color:var(--blue)}.menu{display:none;border:0;background:none;font:700 12px 'DM Mono';color:var(--ink)}
.hero{min-height:720px;display:grid;grid-template-columns:1.15fr .85fr;gap:24px;align-items:center;padding:54px 0 70px}.kicker,.section-label,.pub-venue,.project-type{font:500 10px 'DM Mono';letter-spacing:.13em}.kicker{display:flex;gap:10px;align-items:center;color:var(--blue)}.kicker i{width:9px;height:9px;background:var(--orange);display:inline-block;border-radius:50%}.hero h1{font-size:clamp(58px,7vw,96px);line-height:.92;letter-spacing:-.07em;margin:18px 0 20px}h1 em,h2 em{font-family:'Playfair Display',serif;font-weight:600;color:var(--blue)}.intro{max-width:650px;color:var(--muted);font-size:18px}.intro strong{color:var(--ink)}.intro .intro-highlight{color:var(--blue);font-weight:500}.hero-buttons{display:flex;gap:12px;margin:26px 0}.btn{display:inline-flex;align-items:center;gap:15px;padding:13px 18px;border-radius:4px;font-size:12px;font-weight:700}.btn.blue{background:var(--blue);color:#fff}.btn.blue span{font-size:15px}.btn.outline{border:1px solid #bfc1c7}.quick-links{display:flex;gap:20px;font:500 10px 'DM Mono';color:#626c7e}.quick-links a{border-bottom:1px solid #c6c8cb}
.hero-photo{height:500px;position:relative;display:flex;align-items:center;justify-content:center}.photo-frame{position:relative;width:100%;max-width:420px;height:420px;overflow:hidden;z-index:3;border-radius:18px;box-shadow:none;border:1px solid rgba(23,33,59,.08);margin:0 auto}.photo-frame img{width:100%;height:100%;object-fit:cover;object-position:center center;display:block;filter:saturate(1.04)}.photo-frame:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 54%,rgba(23,33,59,.46))}.photo-caption{position:absolute;z-index:4;bottom:20px;left:20px;right:20px;color:white;display:flex;justify-content:space-between;align-items:end}.photo-caption span{font:500 9px 'DM Mono';letter-spacing:.15em}.photo-caption b{font-size:13px;max-width:150px;text-align:right;line-height:1.25}.shape,.sticker{display:none !important}
.ticker{background:var(--ink);color:#fff;padding:13px 0;overflow:hidden}.ticker-inner{display:flex;justify-content:center;gap:26px;align-items:center;white-space:nowrap;font:500 9px 'DM Mono';letter-spacing:.12em}.ticker b{color:var(--yellow)}
.section{padding:115px 0}.section-label{color:var(--blue);display:flex;align-items:center;gap:10px}.section-label span{color:#9aa0ad}.about-grid{display:grid;grid-template-columns:1fr;gap:24px;margin-top:60px}.about h2,.pub-heading h2,.project-heading h2,.experience h2,.toolkit h2{font-size:clamp(45px,5vw,72px);line-height:.98;letter-spacing:-.06em;margin:0}.about-body .big{font-size:20px;color:#4e596d;margin-top:0}.about-body p{color:var(--muted);max-width:620px}.fact-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:42px}.fact-row div{padding:17px;border-top:3px solid var(--orange);background:#fff4dc}.fact-row div:nth-child(2){border-color:var(--cyan)}.fact-row div:nth-child(3){border-color:var(--violet)}.fact-row strong{display:block;font-size:20px}.fact-row small{font-size:10px;color:var(--muted)}
.research{background:var(--ink);color:white}.light{color:var(--cyan)}.research-head{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:end;margin-top:55px}.research-head h2{font-size:clamp(48px,5vw,74px);line-height:.95;letter-spacing:-.06em;margin:0}.research-head h2 em{color:var(--yellow)}.research-head p{color:#aeb7c7;max-width:540px}.research-cards{display:grid;grid-template-columns:repeat(4, minmax(0, 1fr));gap:16px;margin-top:65px}.r-card{min-height:360px;border-radius:7px;padding:25px;color:var(--ink);position:relative;display:flex;flex-direction:column}.r-card.cyan{background:var(--cyan)}.r-card.orange{background:var(--orange)}.r-card.violet{background:var(--violet)}.r-card .num{font:500 10px 'DM Mono'}.r-card .icon{position:absolute;right:22px;top:18px;font-size:32px}.r-card h3{font-size:26px;line-height:1.02;letter-spacing:-.04em;margin:68px 0 14px}.r-card p{font-size:12px;max-width:330px}.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto}.tags span{border:1px solid rgba(23,33,59,.35);border-radius:30px;padding:5px 8px;font:500 9px 'DM Mono'}
.pub-heading{display:flex;justify-content:space-between;align-items:end;margin-top:55px}.text-link{font:700 11px 'DM Mono';color:var(--blue)}.pub{display:grid;grid-template-columns:100px 1fr auto;gap:30px;border-top:1px solid var(--line);padding:34px 0}.pub.featured{margin-top:45px;background:#fff4dc;border:0;padding:36px;border-left:7px solid var(--orange);grid-template-columns:90px 1fr auto}.pub-year{font:500 13px 'DM Mono';color:#9299a7}.pub-venue{color:var(--blue)}.pub h3{font-size:27px;line-height:1.1;letter-spacing:-.035em;margin:9px 0}.pub p{font-size:13px;color:var(--muted);max-width:750px}.pub-actions{display:flex;gap:17px;margin-top:17px;font-size:10px;font-weight:700;color:var(--blue)}.pub-mark{background:var(--blue);color:#fff;width:90px;height:90px;display:grid;place-items:center;text-align:center;font:700 15px/1 'DM Mono';transform:rotate(4deg)}.pub-mark small{font-size:9px;color:var(--yellow)}.pub-more{border-top:1px solid var(--line);padding:20px 0}.pub-more summary{cursor:pointer;font-size:12px;font-weight:700}.pub-more div{color:var(--muted);font-size:12px;max-width:800px}.pub-more a{color:var(--blue);font-weight:700;text-decoration:none}.pub-more a:hover{text-decoration:underline}
.projects{background:#f0eee7}.project-heading{display:grid;grid-template-columns:1fr 1fr;gap:90px;margin-top:55px}.project-heading p{max-width:500px;color:var(--muted);align-self:end}.project-heading h2 em{color:var(--orange)}.project-list{margin-top:60px}.project{display:grid;grid-template-columns:70px 1fr 35px;gap:25px;padding:27px 0;border-top:1px solid #d2d1cb;align-items:start;transition:.2s}.project:last-child{border-bottom:1px solid #d2d1cb}.project:hover{padding-left:10px;background:#fff9}.project-number{font:500 11px 'DM Mono';color:#8f96a3}.project-type{color:var(--blue)}.project h3{font-size:25px;letter-spacing:-.035em;margin:6px 0}.project p{font-size:12px;color:var(--muted);margin:0;max-width:700px}.arrow{font-size:25px;color:var(--orange)}
.experience-grid{display:grid;grid-template-columns:1fr 1fr;gap:100px;margin-top:60px}.timeline{border-top:1px solid var(--line)}.job{display:grid;grid-template-columns:125px 1fr;gap:20px;padding:23px 0;border-bottom:1px solid var(--line)}.job>span{font:500 9px 'DM Mono';color:#9299a7}.job h3{margin:0;font-size:18px}.job p{margin:2px 0 8px;color:var(--blue);font-size:11px;font-weight:700}.job small{color:var(--muted);font-size:11px}
.contact{background:var(--ink);color:#fff;padding:115px 0}.contact-inner{display:grid;grid-template-columns:180px 1fr;gap:55px}.contact-stamp{border:2px solid var(--yellow);color:var(--yellow);width:125px;height:125px;border-radius:50%;display:grid;place-items:center;text-align:center;font:700 12px/1.05 'DM Mono';transform:rotate(-8deg)}.contact h2{font-size:clamp(50px,6vw,85px);line-height:.92;letter-spacing:-.065em;margin:45px 0 22px}.contact p{max-width:620px;color:#aeb7c7;font-size:14px}.email{display:inline-block;color:var(--yellow);font-size:clamp(20px,3vw,32px);font-weight:700;border-bottom:1px solid #586171;margin-top:12px}.contact-links{display:flex;gap:20px;margin-top:35px;font:500 10px 'DM Mono';color:#aeb7c7}.contact-links a:hover{color:var(--yellow)}
footer{background:#0d1425;color:#687386;font:500 9px 'DM Mono';padding:20px 0}.footer,footer .wrap{display:flex;justify-content:space-between}
@media(max-width:850px){ .wrap{width:min(calc(100% - 32px),1180px)} .navlinks{display:none}.menu{display:block}.navlinks.open{display:flex;position:absolute;left:0;right:0;top:78px;background:var(--paper);padding:20px 28px;flex-direction:column;border-bottom:1px solid var(--line);gap:16px}.hero{grid-template-columns:1fr;gap:30px;padding-top:60px}.hero-photo{height:470px}.photo-frame{height:440px}.about-grid,.research-head,.project-heading,.experience-grid{grid-template-columns:1fr;gap:35px}.research-cards{grid-template-columns:1fr}.r-card{min-height:300px}.pub,.pub.featured{grid-template-columns:1fr;gap:12px}.pub-mark{display:none}.fact-row{grid-template-columns:1fr}.contact-inner{grid-template-columns:1fr;gap:20px}.contact-stamp{margin-left:8px}.section{padding:85px 0}.ticker-inner{justify-content:flex-start;width:max-content}.footer,footer .wrap{flex-direction:column;gap:7px}} 
@media(max-width:520px){ .hero h1{font-size:63px}.hero-photo{height:390px}.photo-frame{height:370px;width:330px}.sticker{left:0;top:85px}.shape.yellow{right:-2px}.shape.coral{left:0}.contact h2{font-size:55px}}"""

SCRIPT = """
  <script>
    const menu = document.querySelector('.menu');
    const nav = document.querySelector('.navlinks');
    menu?.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menu.textContent = open ? 'Close' : 'Menu';
    });
    nav?.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => nav.classList.remove('open')));
  </script>
"""


def node_text(node, default=''):
    if node is None or node.text is None:
        return default
    return node.text.strip()


def node_html(node):
    if node is None:
        return ''
    pieces = []
    if node.text:
        pieces.append(node.text)
    for child in node:
        pieces.append(ET.tostring(child, encoding='unicode', method='html'))
    return ''.join(pieces)


def esc(value):
    return html.escape(str(value), quote=False) if value not in (None, '') else ''


def link_attrs(node):
    href = node.get('href', '#')
    target = node.get('target', '')
    return f'href="{esc(href)}"' + (f' target="{esc(target)}"' if target else '')


root = ET.parse(xml_path).getroot()
header = root.find('./header')
hero = root.find('./hero')
recent = root.find('./recentActivities')
publications = root.find('./publications')
projects = root.find('./projects')
experience = root.find('./experience')
contact = root.find('./contact')
footer = root.find('./footer')

nav_html = ''.join(
    f'<a href="{esc(item.get("href", "#"))}">{esc(item.text or "")}</a>'
    for item in header.findall('./nav/item')
)

buttons_html = ''.join(
    f'<a class="{esc(button.get("class", "btn"))}" href="{esc(button.get("href", "#"))}"{f" target=\"{esc(button.get("target", "_self"))}\"" if button.get("target") else ""}>{node_html(button)}</a>'
    for button in hero.findall('./cta/button')
)

quick_links_html = ''.join(
    f'<a {link_attrs(link)}>{esc(link.text or "")}</a>'
    for link in hero.findall('./quicklinks/link')
)

photo = hero.find('./photo')
photo_src = esc(photo.findtext('src', default='assets/aakash-lake.jpg'))
photo_alt = esc(photo.findtext('alt', default='Aakash image'))
photo_caption = esc(photo.findtext('caption', default='AUSTRIA'))
photo_caption_text = esc(photo.findtext('captionText', default='Curiosity outside the lab.'))

recent_cards_html = ''
for card in recent.findall('./cards/card'):
    keywords = ''.join(
        f'<span>{esc(keyword.text or "")}</span>'
        for keyword in card.findall('./keywords/keyword')
    )
    keywords_html = f'<div class="tags">{keywords}</div>' if keywords else ''
    recent_cards_html += (
        f'<article class="r-card {esc(card.get("class", ""))}">'
        f'<div class="num">{esc(card.findtext("number", default=""))}</div>'
        f'<div class="icon">{esc(card.findtext("icon", default=""))}</div>'
        f'<h3>{esc(card.findtext("title", default=""))}</h3>'
        f'<p>{esc(card.findtext("description", default=""))}</p>'
        f'{keywords_html}'
        f'</article>'
    )

pub_items_html = ''
for item in publications.findall('./items/item'):
    year = esc(item.findtext('year', default=''))
    venue = esc(item.findtext('venue', default=''))
    title = esc(item.findtext('title', default=''))
    desc = esc(item.findtext('description', default=''))
    links = ''.join(
        f'<a {link_attrs(link)}>{esc(link.text or "")}</a>'
        for link in item.findall('./links/link')
    )
    if item.get('featured') == 'true':
        mark = node_html(item.find('./mark'))
        pub_items_html += f'<article class="pub featured"><div class="pub-year">{year}</div><div class="pub-main"><span class="pub-venue">{venue}</span><h3>{title}</h3><p>{desc}</p><div class="pub-actions">{links}</div></div><div class="pub-mark">{mark}</div></article>'
    else:
        pub_items_html += f'<article class="pub"><div class="pub-year">{year}</div><div class="pub-main"><span class="pub-venue">{venue}</span><h3>{title}</h3><p>{desc}</p><div class="pub-actions">{links}</div></div></article>'

more_node = publications.find('./items/more')
more_summary = esc(node_html(more_node.find('./summary')) if more_node is not None and more_node.find('./summary') is not None else 'Earlier publications in statistics & data science')
more_entries_html = ''.join(f'<p>{node_html(e)}</p>' for e in more_node.findall('./entry')) if more_node is not None else ''

proj_html = ''.join(
    f'<a class="project" {link_attrs(item)}><div class="project-number">{esc(item.findtext("number", default=""))}</div><div><span class="project-type">{esc(item.findtext("type", default=""))}</span><h3>{esc(item.findtext("title", default=""))}</h3><p>{esc(item.findtext("description", default=""))}</p></div><span class="arrow">↗</span></a>'
    for item in projects.findall('./items/item')
)

jobs_html = ''.join(
    f'<div class="job"><span>{esc(job.findtext("period", default=""))}</span><div><h3>{esc(job.findtext("role", default=""))}</h3><p>{esc(job.findtext("location", default=""))}</p><small>{esc(job.findtext("description", default=""))}</small></div></div>'
    for job in experience.findall('./jobs/job')
)

contact_links_html = ''.join(
    f'<a {link_attrs(link)}>{esc(link.text or "")}</a>'
    for link in contact.findall('./links/link')
)

logo_html = node_html(header.find('./logo')) or 'Aakash Chowdhury<span>.</span>'
more_link_node = publications.find('./moreLink')
more_link_href = esc(more_link_node.get('href', 'https://orcid.org/0009-0006-1469-763X')) if more_link_node is not None else 'https://orcid.org/0009-0006-1469-763X'
more_link_text = esc(node_html(more_link_node) or 'More on ORCID ↗')

html_output = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(root.findtext('./meta/description', default='Aakash Chowdhury'))}">
  <title>{esc(root.findtext('./meta/title', default='Aakash Chowdhury'))}</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="top-stripe"></div>

  <header class="header">
    <div class="wrap nav">
      <a class="logo" href="#home">{logo_html}</a>
      <button class="menu" aria-label="Open navigation">Menu</button>
      <nav class="navlinks">{nav_html}</nav>
    </div>
  </header>

  <main id="home">
    <section class="hero wrap">
      <div class="hero-copy">
        <div class="kicker"><i></i> {esc(hero.findtext('kicker', default='SECURITY RESEARCHER'))}</div>
        <h1>{node_html(hero.find('./headline'))}</h1>
        <p class="intro">{node_html(hero.find('./intro'))}</p>
        <div class="hero-buttons">{buttons_html}</div>
        <div class="quick-links">{quick_links_html}</div>
      </div>

      <div class="hero-photo">
        <div class="shape yellow"></div>
        <div class="shape coral"></div>
        <div class="photo-frame">
          <img src="{photo_src}" alt="{photo_alt}">
          <div class="photo-caption"><span>{photo_caption}</span><b>{photo_caption_text}</b></div>
        </div>
        <div class="sticker">SIDE-<br>CHANNEL<br>SECURITY</div>
      </div>
    </section>

    <section id="recent-activities" class="about wrap section">
      <div class="section-label"><span>01</span> {esc(recent.findtext('sectionLabel', default='RECENT ACADEMIC ACTIVITIES'))}</div>
      <div class="about-grid">
        <div><h2>{esc(recent.findtext('title', default='Recent academic activity'))}</h2></div>
        <div class="about-body">
          <p class="big">{esc(recent.findtext('description', default=''))}</p>
          <div class="research-cards">{recent_cards_html}</div>
        </div>
      </div>
    </section>

    <section id="publications" class="publications wrap section">
      <div class="section-label"><span>02</span> {esc(publications.findtext('sectionLabel', default='PUBLICATIONS'))}</div>
      <div class="pub-heading">
        <h2>{node_html(publications.find('./title'))}</h2>
        <a href="{more_link_href}" target="_blank" class="text-link">{more_link_text}</a>
      </div>
      {pub_items_html}
      <details class="pub-more">
        <summary>{more_summary}</summary>
        <div>{more_entries_html}</div>
      </details>
    </section>

    <section id="projects" class="projects section">
      <div class="wrap">
        <div class="section-label"><span>03</span> {esc(projects.findtext('sectionLabel', default='OPEN SOURCE'))}</div>
        <div class="project-heading">
          <h2>{node_html(projects.find('./title'))}</h2>
          <p>{esc(projects.findtext('description', default=''))}</p>
        </div>
        <div class="project-list">{proj_html}</div>
      </div>
    </section>

    <section id="experience" class="experience wrap section">
      <div class="section-label"><span>04</span> {esc(experience.findtext('sectionLabel', default='EXPERIENCE'))}</div>
      <div class="experience-grid">
        <div><h2>{node_html(experience.find('./title'))}</h2></div>
        <div class="timeline">{jobs_html}</div>
      </div>
    </section>

    <section id="contact" class="contact">
      <div class="wrap contact-inner">
        <div class="contact-stamp">LET'S<br>TALK<br>↘</div>
        <div>
          <div class="section-label light"><span>05</span> {esc(contact.findtext('sectionLabel', default='CONTACT'))}</div>
          <h2>{node_html(contact.find('./title'))}</h2>
          <p>{esc(contact.findtext('description', default=''))}</p>
          <a class="email" href="{esc(contact.find('./email').get('href', '#'))}">{esc(contact.findtext('email', default='aakchowdhury94@gmail.com'))}</a>
          <div class="contact-links">{contact_links_html}</div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="wrap"><span>{esc(footer.findtext('copyright', default='© 2026 Aakash Chowdhury'))}</span><span>{esc(footer.findtext('tagline', default='Side-channel analysis · Statistics · Security'))}</span></div>
  </footer>
  {SCRIPT}
</body>
</html>
'''

html_path.write_text(html_output, encoding='utf-8')
print(f'Generated {html_path.name}')
