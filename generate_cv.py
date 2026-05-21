#!/usr/bin/env python3
"""Generate cv.typ from the website's markdown files using the neat-cv Typst package.

Reads structured data from pages/about.md, then generates a complete Typst CV file
using the neat-cv package for styling.

Usage: python generate_cv.py
Output: cv.typ (compile with: typst compile cv.typ cv.pdf --font-path ./fonts)
"""

import re
from pathlib import Path

# ============================================================================
# Utility functions
# ============================================================================


def read_file(base, filename):
    """Read a markdown file, stripping YAML frontmatter."""
    text = (base / filename).read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3 :]
    return text.strip()


def strip_markdown(text):
    """Remove markdown formatting, returning plain text."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<https?://[^>]+>", "", text)
    return text.strip()


def parse_table(text):
    """Parse a markdown table into a list of row dicts."""
    lines = [l.strip() for l in text.strip().split("\n") if l.strip().startswith("|")]
    if len(lines) < 3:
        return []

    def split_row(line):
        cells = [c.strip() for c in line.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        return cells

    headers = split_row(lines[0])
    rows = []
    for line in lines[2:]:
        cells = split_row(line)
        row = {}
        for i, h in enumerate(headers):
            row[h] = cells[i] if i < len(cells) else ""
        rows.append(row)
    return rows


def extract_section(text, heading):
    """Extract content between a heading and the next heading of same/higher level or ---."""
    escaped = re.escape(heading)
    m = re.search(rf"^{escaped}\s*$", text, re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    level = len(re.match(r"^#+", heading).group())
    end_pat = rf"^(?:#{{{1},{level}}}\s|---\s*$)"
    end_m = re.search(end_pat, text[start:], re.MULTILINE)
    if end_m:
        return text[start : start + end_m.start()].strip()
    return text[start:].strip()


def parse_bullets(text):
    """Parse bullet list items, joining continuation lines."""
    items = []
    current = None
    for line in text.split("\n"):
        m = re.match(r"^[\-\*]\s+(.+)", line)
        if m:
            if current is not None:
                items.append(current)
            current = m.group(1)
        elif current is not None and line.strip():
            current += " " + line.strip()
    if current is not None:
        items.append(current)
    return items


def typst_escape(text):
    """Escape special Typst characters in text."""
    if not text:
        return ""
    text = text.replace("#", "\\#")
    text = text.replace("@", "\\@")
    text = text.replace("$", "\\$")
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    return text


# ============================================================================
# Main generation
# ============================================================================


def gen_preamble():
    """Generate Typst preamble with neat-cv import and author config."""
    return """#import "@preview/neat-cv:1.0.0": (
  contact-info, cv, cv-thin-side, cv-with-side, email-link, entry, item-pills,
  item-with-level, publications, reference, social-links, thin-label,
  thin-metrics,
)

#set text(lang: "fr")

#show: cv.with(
  author: (
    firstname: "Lucas",
    lastname: "Ravelonjaka",
    email: "lucasravelonjaka@gmail.com",
    address: [Île-de-France (mobile)],
    phone: "+33 6 63 80 74 97",
    position: ("Géomaticien",),
    website: "https://hoperror.github.io/portfolio_SIG_Ravelonjaka/",
    github: "hoperror",
    linkedin: "lucasravelonjaka",
  ),
  profile-picture: image("photopro_lucas.jpg"),
  accent-color: rgb("#2b6cb0"),
  header-color: rgb("#1a365d"),
  paper-size: "a4",
  body-font-size: 9.5pt,
)

// Reduce spacing between sections and entries to fit on one page
#show heading: set block(above: 0.6em, below: 0.4em)
#set block(spacing: 0.5em)"""


def gen_sidebar_content(about):
    """Generate the sidebar content - all on one page, no colbreak."""
    lines = []

    # --- Profil ---
    m = re.search(r"^#\s+.+$", about, re.MULTILINE)
    if m:
        start = m.end()
        end_m = re.search(r"^(?:##\s|---\s*$)", about[start:], re.MULTILINE)
        if end_m:
            profil_text = about[start : start + end_m.start()].strip()
        else:
            profil_text = about[start:].strip()
        if profil_text:
            lines.append("  = Profil")
            lines.append(f"  {typst_escape(profil_text)}")
            lines.append("")

    # --- Contact ---
    lines.append("  = Contact")
    lines.append("  #contact-info()")
    lines.append("")

    # --- Informations ---
    lines.append("  = Informations")
    lines.append("  Permis B")
    lines.append("")
    lines.append("  Disponible dès sept. 2026")
    lines.append("")

    # --- Langues (dans la sidebar, sous informations) ---
    section = extract_section(about, "## Langues")
    rows = parse_table(section)
    if rows:
        lines.append("  = Langues")
        level_map = {
            "Bilingue": 5,
            "Langue maternelle": 5,
            "C2": 5,
            "C1": 4,
            "B2": 3.5,
            "B1": 3,
            "A2": 2,
            "A1": 1,
            "Bases": 1.5,
        }
        for row in rows:
            langue = strip_markdown(row.get("Langue", ""))
            niveau = strip_markdown(row.get("Niveau", ""))
            # Skip Russe to save space
            if langue.lower() == "russe":
                continue
            score = level_map.get(niveau, 3)
            lines.append(f'  #item-with-level("{langue}", {score}, subtitle: "{niveau}")')
        lines.append("")

    # --- Centres d'intérêt ---
    section = extract_section(about, "## Centres d'intérêt")
    if section:
        bullets = parse_bullets(section)
        if bullets:
            # Extract detailed items from after the colon
            all_items = []
            for b in bullets:
                if ":" in b:
                    details = b.split(":", 1)[1].strip()
                    detail_list = [d.strip() for d in details.split(",")]
                    all_items.extend(detail_list)
                else:
                    all_items.append(b.strip())
            items_quoted = ", ".join(f'"{typst_escape(i)}"' for i in all_items if i)
            lines.append("  = Centres d'intérêt")
            lines.append(f"  #item-pills(({items_quoted},))")
            lines.append("")

    # --- Social links at bottom ---
    lines.append("  #v(1fr)")
    lines.append("  #social-links()")

    return "\n".join(lines)


def gen_main_content(about):
    """Generate the main body content - order: expériences, formation, projets, compétences."""
    lines = []

    # --- 1. Expériences professionnelles (en premier) ---
    lines.append("  = Expériences professionnelles")
    lines.append("")

    # Hardcoded entries with correct short dates and Plaine Commune periods
    experiences = [
        {
            "title": "Géomaticien apprenti",
            "date": "août 2024 – août 2026",
            "institution": "Port de Boulogne-sur-Mer—Calais, Région Hauts-de-France",
        },
        {
            "title": "Chargé d'étude stagiaire",
            "date": "mars 2024 – sept. 2024",
            "institution": "Direction des données, des études et des connaissances, Conseil départemental de la Seine-Saint-Denis",
        },
        {
            "title": "Géomaticien",
            "date": "juil. 2023 – sept. 2023",
            "institution": "Observatoire EPT Plaine Commune",
        },
        {
            "title": "Chargé d'études stagiaire",
            "date": "juin 2023 – juil. 2023",
            "institution": "Observatoire EPT Plaine Commune",
        },
    ]

    for exp in experiences:
        lines.append(f"  #entry(")
        lines.append(f'    title: "{typst_escape(exp["title"])}",')
        lines.append(f'    date: "{typst_escape(exp["date"])}",')
        lines.append(f'    institution: "{typst_escape(exp["institution"])}",')
        lines.append(f'    "",')
        lines.append(f"  )")
        lines.append("")

    # --- 2. Formation ---
    section = extract_section(about, "## Formation")
    rows = parse_table(section)
    if rows:
        lines.append("  = Formation")
        lines.append("")
        for row in rows:
            periode = strip_markdown(row.get("Période", ""))
            diplome = strip_markdown(row.get("Diplôme", ""))
            etablissement = strip_markdown(row.get("Établissement", ""))
            lines.append(f"  #entry(")
            lines.append(f'    title: "{typst_escape(diplome)}",')
            lines.append(f'    date: "{typst_escape(periode)}",')
            lines.append(f'    institution: "{typst_escape(etablissement)}",')
            lines.append(f'    "",')
            lines.append(f"  )")
            lines.append("")

    # --- 3. Projets SIG (sélection) ---
    lines.append("  = Projets SIG (sélection)")
    lines.append("")

    projects = [
        {
            "title": "Outil cartographique portuaire",
            "date": "2026",
            "institution": "Port de Boulogne-sur-Mer—Calais",
            "desc": [
                "Application web de suivi des interventions sur le domaine portuaire",
                "Django, PostgreSQL/PostGIS, Leaflet.js",
            ],
        },
        {
            "title": "Portail Laridés",
            "date": "2025",
            "institution": "Port de Boulogne-sur-Mer—Calais",
            "desc": [
                "Portail cartographique de suivi des colonies de mouettes et goélands",
                "ArcGIS Online, Experience Builder",
            ],
        },
        {
            "title": "Tiques et paysages français",
            "date": "2025-2026",
            "institution": "Université Paris 8 / INRAE CiTIQUE",
            "desc": [
                "Analyse multivariée (ACP, k-means) des paysages associés aux piqûres de tiques",
                "Python, R, QGIS",
            ],
        },
        {
            "title": "Vidéoprotection et délinquance de rue",
            "date": "2026",
            "institution": "Université Paris 8",
            "desc": [
                "Analyse SIG de l'impact de la vidéoprotection sur la sécurité à GPSO",
                "Python/Pandas, QGIS, PyQGIS, Open Data",
            ],
        },
    ]

    for p in projects:
        lines.append(f"  #entry(")
        lines.append(f'    title: "{typst_escape(p["title"])}",')
        lines.append(f'    date: "{typst_escape(p["date"])}",')
        lines.append(f'    institution: "{typst_escape(p["institution"])}",')
        lines.append(f"  )[")
        for d in p["desc"]:
            lines.append(f"    - {typst_escape(d)}")
        lines.append(f"  ]")
        lines.append("")

    # --- 4. Compétences (en bas du corps principal) ---
    section = extract_section(about, "## Compétences")
    rows = parse_table(section)
    if rows:
        lines.append("  = Compétences")
        lines.append("")
        for row in rows:
            domaine = strip_markdown(row.get("Domaine", ""))
            technologies = strip_markdown(row.get("Technologies", ""))
            tech_list = [t.strip() for t in technologies.split(",")]
            tech_quoted = ", ".join(f'"{t}"' for t in tech_list if t)
            lines.append(f"  *{domaine}* :")
            lines.append(f"  #item-pills(({tech_quoted},))")
            lines.append("")

    return "\n".join(lines)


# ============================================================================
# Main
# ============================================================================


def main():
    """Read website markdown files and generate cv.typ."""
    base = Path(__file__).parent
    pages = base / "pages"

    about = read_file(pages, "about.md")

    sidebar = gen_sidebar_content(about)
    main_content = gen_main_content(about)

    output = f"""{gen_preamble()}


#cv-with-side[
{sidebar}
][
{main_content}
]
"""

    out_path = base / "cv.typ"
    out_path.write_text(output, encoding="utf-8")
    print(f"Generated {out_path} ({len(output):,} bytes)")


if __name__ == "__main__":
    main()