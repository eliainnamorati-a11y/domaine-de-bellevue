#!/usr/bin/env python3
"""One-off: tag index.html for FR/EN and generate js/i18n.js.

E(key, open_tag, prefix, en, fr=None, count=1)
    Finds `open_tag` immediately followed by text starting with `prefix`, up to the matching
    closing tag. Adds data-i18n="key". FR = the existing French text unless `fr` is given.
A(key, attr, old_value, en, fr=None, count=1)
    Finds attr="old_value", rewrites as data-i18n-attr="attr:key" attr="fr".
"""
import html
import json
import re
import sys

PATH = 'index.html'
src = open(PATH, encoding='utf-8').read()

FR, EN = {}, {}
errors = []


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def E(key, open_tag, prefix, en, fr=None, count=1):
    global src
    tag = re.match(r'<(\w+)', open_tag).group(1)
    pat = re.compile(re.escape(open_tag) + r'(\s*' + re.escape(prefix) + r'.*?)(</' + tag + r'>)', re.S)
    matches = list(pat.finditer(src))
    if len(matches) != count:
        errors.append(f'E {key}: expected {count}, found {len(matches)}  [{open_tag} {prefix[:40]}]')
        return
    fr_val = fr if fr is not None else norm(matches[0].group(1))
    FR[key], EN[key] = fr_val, en
    new_open = open_tag[:-1] + f' data-i18n="{key}">'
    src = pat.sub(lambda m: new_open + fr_val + m.group(2), src)


def A(key, attr, old, en, fr=None, count=1):
    global src
    needle = f'{attr}="{old}"'
    n = src.count(needle)
    if n != count:
        errors.append(f'A {key}: expected {count}, found {n}  [{needle[:60]}]')
        return
    fr_val = fr if fr is not None else html.unescape(old)
    FR[key], EN[key] = fr_val, en
    src = src.replace(needle, f'data-i18n-attr="{attr}:{key}" {attr}="{html.escape(fr_val, quote=True)}"')


# ------------------------------------------------------------------ meta + already-tagged header/hero
FR.update({
    'meta.title': 'Domaine de Bellevue | Villas de luxe près de Nyon',
    'meta.description': 'Nouveau projet immobilier de luxe à Trélex, près de Nyon et Genève : villas neuves de prestige, design contemporain et cadre privilégié. Dernières disponibilités : Villas 1, 2 et 3.',
    'nav.contact': 'Contact', 'nav.villas': 'Les Villas', 'nav.plan': 'Plan &amp; Disponibilités',
    'nav.custom': 'Sur Mesure', 'nav.project': 'Le Projet', 'nav.architecture': 'Architecture',
    'nav.location': 'Situation', 'nav.lifestyle': 'Art de vivre', 'nav.brochure': 'Brochure &amp; Plans',
    'hero.location': 'Trélex · Région de Nyon',
    'hero.title': 'Huit villas d’exception<br>sur les hauteurs du Léman',
    'hero.cta': 'Découvrir les villas', 'hero.scroll': 'Défiler vers le bas',
    'form.send': 'Envoyer', 'form.sent': 'Envoyé avec succès',
})
EN.update({
    'meta.title': 'Domaine de Bellevue | Luxury Villas near Nyon',
    'meta.description': 'New luxury residential project in Trélex, near Nyon and Geneva: prestigious new-build villas, contemporary design and an exceptional setting. Last availabilities: Villas 1, 2 and 3.',
    'nav.contact': 'Contact', 'nav.villas': 'The Villas', 'nav.plan': 'Site Plan &amp; Availability',
    'nav.custom': 'Bespoke', 'nav.project': 'The Project', 'nav.architecture': 'Architecture',
    'nav.location': 'Location', 'nav.lifestyle': 'Lifestyle', 'nav.brochure': 'Brochure &amp; Plans',
    'hero.location': 'Trélex · Nyon Region',
    'hero.title': 'Eight exceptional villas<br>above Lake Geneva',
    'hero.cta': 'Discover the villas', 'hero.scroll': 'Scroll down',
    'form.send': 'Send', 'form.sent': 'Sent successfully',
})

# ------------------------------------------------------------------ VILLAS
E('villas.eyebrow', '<h2 class="sub-title">', 'THE VILLAS', 'THE VILLAS', fr='LES VILLAS')
E('villas.title', '<h1 class="main-title">', 'The perfect balance', 'The perfect balance between style and comfort',
  fr='L’équilibre parfait entre style et confort')
E('villas.intro', '<p class="section-text">', 'Dernières opportunités',
  'The last exclusive opportunities on the estate, <strong>Villas 1, 2 and 3</strong> embody the perfect harmony of contemporary architecture, exceptional volumes and landscape integration. Set in a commanding position on the most generous plots, they offer unique views over Lake Geneva, the Alps and the surrounding woodland.')
E('villa.status', '<span class="villa-status-chip available">', 'Available on Request', 'Available on request',
  fr='Disponible sur demande', count=3)
E('villa.pdf', '<a href="docs/Domaine-de-Bellevue-Lot-1-.pdf" target="_blank" class="villa-btn-pdf-stacked">', 'Télécharger',
  'Download plans (PDF)', fr='Télécharger les plans (PDF)')
E('villa.pdf', '<a href="docs/Domaine-de-Bellevue-Lot-2.pdf" target="_blank" class="villa-btn-pdf-stacked">', 'Télécharger',
  'Download plans (PDF)', fr='Télécharger les plans (PDF)')
E('villa.pdf', '<a href="docs/Domaine-de-Bellevue-Lot-3.pdf" target="_blank" class="villa-btn-pdf-stacked">', 'Télécharger',
  'Download plans (PDF)', fr='Télécharger les plans (PDF)')

E('villa1.lead', '<p class="villa-stacked-lead">', 'Position dominante',
  'Commanding position at the top of the estate (top left of the plan). A vast, unoverlooked 939 m² private plot with panoramic views of Lake Geneva and the Alps.')
E('villa2.lead', '<p class="villa-stacked-lead">', 'La plus grande surface',
  'The largest built area on the estate (376 m² SBP). Triple south / south-west aspect and a suspended terrace of more than 55 m² extending the reception rooms.')
E('villa3.lead', '<p class="villa-stacked-lead">', 'Adossée au cordon',
  'Backing onto a protected natural woodland belt. A generous 541 m² plot with a basement of more than 100 m², fully customisable (wellness, wine cellar, home cinema).')

for old in ['Cliquer pour agrandir la vue principale', 'Cliquer pour agrandir la vue lac', 'Cliquer pour agrandir la vue jardin',
            'Cliquer pour agrandir la vue façade', 'Cliquer pour agrandir la vue terrasse', 'Cliquer pour agrandir la vue intérieure',
            'Cliquer pour agrandir la vue lisière', 'Cliquer pour agrandir la vue environnement', 'Cliquer pour agrandir la vue séjour']:
    A('villa.zoom', 'title', old, 'Click to enlarge', fr='Cliquer pour agrandir')

LBL = '<span class="triptych-label">'
E('v1.img1', LBL, 'Architecture &amp; Façade', 'Architecture &amp; façade', fr='Architecture &amp; façade')
E('v1.img2', LBL, 'Vue Lac Léman', 'Lake Geneva &amp; Alps view', fr='Vue lac Léman &amp; Alpes')
E('v1.img3', LBL, 'Jardin 939', '939 m² garden (pool area)', fr='Jardin 939 m² (emplacement piscine)')
E('v2.img1', LBL, 'Façade Sud-Ouest', 'South-west façade', fr='Façade sud-ouest')
E('v2.img2', LBL, 'Terrasse Suspendue', 'Suspended terrace &gt; 55 m²', fr='Terrasse suspendue &gt; 55 m²')
E('v2.img3', LBL, 'Volumes &amp; Baies', 'Volumes &amp; picture windows', fr='Volumes &amp; baies vitrées')
E('v3.img1', LBL, 'Façade &amp; Lisière', 'Façade &amp; woodland edge', fr='Façade &amp; lisière boisée')
E('v3.img2', LBL, 'Cadre Naturel', 'Unspoilt natural setting', fr='Cadre naturel préservé')
E('v3.img3', LBL, 'Séjour Ouvert', 'Living room opening onto the 541 m² garden', fr='Séjour ouvert sur jardin 541 m²')

A('v1.alt1', 'alt', 'Villa 1 - Architecture & Façade Contemporaine', 'Villa 1 - Contemporary architecture & façade')
A('v1.alt2', 'alt', 'Villa 1 - Vue Lac Léman et Alpes', 'Villa 1 - View of Lake Geneva and the Alps')
A('v1.alt3', 'alt', 'Villa 1 - Terrain 939 m² & Emprise Piscine', 'Villa 1 - 939 m² plot & pool area')
A('v2.alt1', 'alt', 'Villa 2 - Façade Sud-Ouest Ensoleillée', 'Villa 2 - Sunny south-west façade')
A('v2.alt2', 'alt', 'Villa 2 - Terrasse Suspendue Panoramique', 'Villa 2 - Panoramic suspended terrace')
A('v2.alt3', 'alt', 'Villa 2 - Volumes de Vie Lumineux', 'Villa 2 - Bright living spaces')
A('v3.alt1', 'alt', 'Villa 3 - Façade Contemporaine et Arbres Centenaires', 'Villa 3 - Contemporary façade and century-old trees')
A('v3.alt2', 'alt', 'Villa 3 - Environnement Naturel Paisible', 'Villa 3 - Peaceful natural surroundings')
A('v3.alt3', 'alt', 'Villa 3 - Séjour Ouvert sur le Jardin Privatif', 'Villa 3 - Living room opening onto the private garden')

SL = '<span class="spec-label">'
E('spec.sbp', SL, 'Surface Brute', 'Gross floor area (SBP)', fr='Surface brute (SBP)', count=3)
E('spec.living', SL, 'Surface Habitable', 'Living area', fr='Surface habitable', count=3)
E('spec.garden', SL, 'Jardin Privatif', 'Private garden', fr='Jardin privatif', count=3)
E('spec.features', SL, 'Aménagements', 'Features', fr='Aménagements')
E('spec.terrace', SL, 'Terrasse', 'Terrace', fr='Terrasse')
E('spec.basement', SL, 'Sous-Sol', 'Flexible basement', fr='Sous-sol modulable')
E('spec.pool', '<span class="spec-val">', 'Piscine Faisable', 'Pool possible', fr='Piscine réalisable')
E('spec.record', '<span class="spec-val">', '376 m² (Record)', '376 m² (largest on the estate)', fr='376 m² (record du domaine)')

A('loc.hint_title', 'title', 'Cliquer pour localiser sur le Masterplan interactif', 'Click to locate on the interactive site plan',
  fr='Cliquer pour localiser sur le plan interactif', count=3)
E('loc.title', '<span class="locator-title">', 'Emplacement Masterplan', 'Location on site plan', fr='Emplacement sur le plan', count=3)
E('loc.v1', '<strong class="locator-name">', 'Villa 1', 'Villa 1 • Top left', fr='Villa 1 • En haut à gauche')
E('loc.v2', '<strong class="locator-name">', 'Villa 2', 'Villa 2 • Top centre', fr='Villa 2 • En haut au centre')
E('loc.v3', '<strong class="locator-name">', 'Villa 3', 'Villa 3 • Top right', fr='Villa 3 • En haut à droite')
E('loc.hint', '<span class="locator-hint">', 'Voir sur le plan', 'View on the site plan ↓', count=3)
for i in (1, 2, 3):
    A(f'loc.alt{i}', 'alt', f'Emplacement Villa {i} sur plan', f'Location of Villa {i} on the plan')
A('loc.v1', 'title', 'Villa 1 • Top Left', 'Villa 1 • Top left', fr='Villa 1 • En haut à gauche')
A('loc.v2', 'title', 'Villa 2 • Top Center', 'Villa 2 • Top centre', fr='Villa 2 • En haut au centre')
A('loc.v3', 'title', 'Villa 3 • Top Right', 'Villa 3 • Top right', fr='Villa 3 • En haut à droite')

# ------------------------------------------------------------------ PLAN
E('plan.eyebrow', '<h2 class="sub-title">', 'SITE MAP', 'SITE PLAN', fr='PLAN DU DOMAINE')
E('plan.title', '<h1 class="main-title">', 'Availability', 'Availability &amp; interactive site plan',
  fr='Disponibilités &amp; plan interactif')
A('plan.alt0', 'alt', 'Plan Général Domaine de Bellevue', 'Domaine de Bellevue site plan')
A('plan.alt1', 'alt', 'Lot 1 (Top Left - 939 m²)', 'Lot 1 (top left - 939 m²)', fr='Lot 1 (en haut à gauche - 939 m²)')
E('plan.th_sbp', '<th>', 'SBP Total', 'Total SBP', fr='SBP totale')
E('plan.th_living', '<th>', 'SBP Habitable', 'Living SBP', fr='SBP habitable')
E('plan.th_garden', '<th>', 'Garden', 'Garden', fr='Jardin')
E('plan.th_price', '<th>', 'Price', 'Price', fr='Prix')
E('plan.request', '<td>', 'On Request', 'On request', fr='Sur demande', count=3)
E('plan.reserved', '<td>', 'Reserve', 'Reserved', fr='Réservée', count=2)
E('plan.sold', '<td>', 'Sold', 'Sold', fr='Vendue', count=3)
for i in (1, 2, 3):
    A(f'plan.pdf{i}', 'title', f'Plans officiels Lot {i}', f'Official plans, Lot {i}')
E('plan.note_sbp', '<p>', '<strong>SBP :</strong>',
  '<strong>SBP:</strong> Gross floor area calculated according to the cantonal standards of Vaud.')
E('plan.disclaimer', '<p>', 'Toutes les informations',
  'All information and visuals shown are non-contractual and provided for illustration only. Furniture and finishes may differ from the final project. Changes and adjustments remain reserved until completion of construction.')

# ------------------------------------------------------------------ PERSONNALISATION
E('custom.eyebrow', '<h2 class="sub-title">', 'SUR MESURE', 'BESPOKE')
E('custom.title', '<h1 class="main-title">', 'Personnalisation', 'Full customisation at an early stage',
  fr='Personnalisation intégrale en phase initiale')
E('custom.intro', '<p class="section-text">', 'Le chantier se trouvant',
  'With construction currently in its initial phase, buyers of Villas 1, 2 and 3 have the rare opportunity to design and adapt their interiors in close collaboration with the architecture studio.')
E('custom.h1', '<h4>', 'Modularité', 'Flexible layouts &amp; volumes', fr='Modularité des cloisons &amp; volumes')
E('custom.p1', '<p>', 'Redéfinissez', 'Freely redefine the floor plan: choose between 4, 5 or 6 bedrooms, create a spacious dual-aspect master suite with a bespoke walk-in wardrobe, a glazed study or a reading lounge.')
E('custom.h2', '<h4>', 'Cuisines Suisses', 'Swiss kitchens &amp; premium appliances', fr='Cuisines suisses &amp; électroménager haut de gamme')
E('custom.p2', '<p>', 'Profitez de budgets', 'Benefit from generous allowances with our outstanding partners to design your ideal kitchen: islands in Dekton or natural marble, Miele or Gaggenau appliances, or Bora extractor hobs.')
E('custom.h3', '<h4>', 'Matériaux Nobles', 'Fine materials &amp; designer bathrooms', fr='Matériaux nobles &amp; salles de bains de style')
E('custom.p3', '<p>', 'Sélectionnez personnellement', 'Personally select your finishes: brushed solid oak parquet (wide planks or herringbone), large-format Italian porcelain tiles, walk-in showers and concealed fittings.')
E('custom.h4', '<h4>', 'Sous-Sol Privatif', 'Versatile private basement (&gt; 100 m²)', fr='Sous-sol privatif polyvalent (&gt; 100 m²)')
E('custom.p4', '<p>', 'Le niveau inférieur', 'The entire lower level offers complete freedom of layout: a spa with sauna and hammam, a home cinema, a traditional Vaud carnotzet or a fitness room.')
E('custom.h5', '<h4>', 'Piscine Extérieure', 'Outdoor pool &amp; landscaping', fr='Piscine extérieure &amp; aménagements paysagers')
E('custom.p5', '<p>', 'Grâce aux dimensions', 'Thanks to the generous size of plots 1, 2 and 3, a heated in-ground pool with a submerged cover, a bioclimatic pergola and a summer kitchen are technically feasible.')
E('custom.h6', '<h4>', 'Accompagnement', 'Dedicated architectural support', fr='Accompagnement architectural dédié')
E('custom.p6', '<p>', 'Notre équipe', 'Our project management team and the project architect guide you step by step through personal meetings to bring every detail of your vision to life.')
E('custom.cta', '<a href="#contact" class="villa-btn-pdf" style="padding: 12px 30px; display: inline-block;">', 'Échanger',
  'Discuss your customisation wishes')

# ------------------------------------------------------------------ DISPONIBILITÉ / PROJET / ARCHITECTURE
E('avail.eyebrow', '<h2 class="sub-title">', 'DISPONIBILITÉ 2027', 'AVAILABLE IN 2027')
E('avail.title', '<h1 class="main-title">', 'Domaine résidentiel exclusif', 'An exclusive residential estate in Trélex')
E('avail.text', '<p class="section-text">', 'À une adresse privilégiée',
  'At a privileged address on the peaceful heights of Trélex lies a rare ensemble of eight exceptional villas. Conceived as a true private estate, the project combines refinement, discretion and high-end comfort. Nestled in greenery, some villas even enjoy open views of Lake Geneva, offering a living environment that is both exclusive and harmonious.')
A('avail.alt', 'alt', 'Domaine de Bellevue Trélex - Vue Aérienne', 'Domaine de Bellevue Trélex - aerial view')

E('project.eyebrow', '<h2 class="sub-title">', 'LE PROJET', 'THE PROJECT')
E('project.title', '<h1 class="main-title">', 'Un domaine pensé', 'An estate designed for you')
E('project.text', '<p class="section-text">', 'Ce domaine résidentiel',
  'This residential estate stands out for its generous spaces, contemporary architecture and prestigious finishes. Surrounded by trees and sheltered from any bustle, the villas offer privacy and serenity. Each home is designed for modern living: bright volumes, spacious private terraces and intelligent flexibility. More than just a residence, it is an elegant and peaceful community at the heart of an exceptional setting.')
A('project.alt', 'alt', 'Le Projet Domaine de Bellevue', 'The Domaine de Bellevue project')

E('arch.title', '<h1 class="main-title">', 'Des espaces pensés', 'Spaces designed for living with style and serenity')
E('arch.text', '<p class="section-text">', 'Les villas s’intègrent',
  'The villas blend elegantly into the landscape, combining modern lines with noble materials. Natural stone, panoramic glazing and high-end finishes shape timeless interiors where every detail exudes quality and sophistication. Living spaces open onto the surrounding nature, creating a symbiosis between indoor comfort and outdoor beauty.')
A('arch.alt', 'alt', 'Architecture &amp; Design de Prestige', 'Prestige architecture &amp; design')

# ------------------------------------------------------------------ SITUATION
E('loc.eyebrow', '<h2 class="sub-title">', 'Expérience résidentielle', 'An exclusive residential experience in Trélex')
E('loc.text1', '<p class="section-text">', 'Situé dans un quartier',
  'Located in a sought-after, quiet residential area, the estate combines proximity to nature with easy access to the city. Just a few minutes from Nyon and less than 20 minutes from Geneva International Airport, residents enjoy a strategic location. Lausanne and Geneva are easily reached, as are the ski resorts of the Jura and the Alps.')
E('loc.text2', '<p class="section-text">', 'À deux pas',
  'Close by, the Parcours Vita fitness trail (7 minutes on foot), forests and vineyards invite relaxation and outdoor activities. Families will appreciate the proximity of prestigious local and international schools, offering both the Swiss Maturité and recognised international diplomas, ensuring an excellent educational environment for their children.')
E('loc.car', '<span>', 'En Voiture', 'By car', fr='En voiture')
E('loc.transport', '<span>', 'Transports', 'Public transport', fr='Transports publics')
A('loc.car_alt', 'alt', 'Voiture', 'Car')
A('loc.transport_alt', 'alt', 'Transports', 'Public transport', fr='Transports publics')
E('loc.airport', '<td>', 'Genève Aéroport', 'Geneva Airport')
E('loc.hour', '<td>', '1 hr', '1 hr', fr='1 h')
E('loc.school', '<td>', 'Ecole Moser', 'Ecole Moser', fr='École Moser')
A('loc.alt', 'alt', 'Vue Aérienne Domaine de Bellevue', 'Aerial view of Domaine de Bellevue')

# ------------------------------------------------------------------ LIFESTYLE
E('life.eyebrow', '<h2 class="sub-title">', 'LIFESTYLE', 'LIFESTYLE', fr='STYLE DE VIE')
E('life.title', '<h1 class="main-title">', 'Art de vivre', 'The art of living')
A('life.prev', 'aria-label', 'Précédent', 'Previous')
A('life.next', 'aria-label', 'Suivant', 'Next')
E('life.h1', '<h3>', 'UN QUARTIER VIVANT', 'A VIBRANT NEIGHBOURHOOD')
E('life.p1', '<p>', 'À proximité de Trélex', 'Near Trélex, enjoy a wide choice of restaurants and cafés, as well as shops, services and places to meet. The neighbouring towns of the Nyon region, Geneva and Lausanne add a rich and diverse cultural, culinary and social scene.')
E('life.h2', '<h3>', 'CADRE DE VIE FAMILIAL', 'A FAMILY-FRIENDLY SETTING')
E('life.p2', '<p>', 'La proximité d’écoles', 'High-quality schools nearby make everyday life easier for parents and reassure them about their children’s future. A wide range of activities — sport, culture and green spaces — creates a safe and pleasant environment where young people can thrive.')
E('life.h3', '<h3>', 'UNE RÉGION AUX MILLE', 'A REGION OF A THOUSAND PLEASURES')
E('life.p3', '<p>', 'Entre lac et montagnes', 'Between lake and mountains, the region invites both relaxation and adventure. Water sports on Lake Geneva, Alpine hikes, bike rides through the Vaud countryside and, in winter, the ski slopes of St-Cergue just 15 minutes away offer a unique quality of life through the seasons.')
E('life.h4', '<h3>', 'AU CŒUR DE LA NATURE', 'IN THE HEART OF NATURE')
E('life.p4', '<p>', 'Parcours Vita Trélex', 'The Parcours Vita Trélex, just a 5-minute walk away, joins the other parks and green spaces nearby, offering an ideal setting for exercise, relaxation and outdoor activities. The immediate proximity of nature and forest is ideal for pet owners and invites lovely walks in the open air.')
A('life.alt1', 'alt', 'Un quartier vivant', 'A vibrant neighbourhood')
A('life.alt2', 'alt', 'Cadre de vie familial', 'A family-friendly setting')
A('life.alt3', 'alt', 'Une région aux mille plaisirs', 'A region of a thousand pleasures')
A('life.alt4', 'alt', 'Au cœur de la nature', 'In the heart of nature')

# ------------------------------------------------------------------ BROCHURE / CONTACT / FOOTER / LIGHTBOX
E('dl', '<a href="docs/DOMAINE-DE-BELLEVUE-2026-1.pdf" target="_blank">', 'DOWNLOAD', 'DOWNLOAD', fr='TÉLÉCHARGER')
E('dl', '<a href="docs/Domaine-de-Bellevue-Plans.pdf" target="_blank">', 'DOWNLOAD', 'DOWNLOAD', fr='TÉLÉCHARGER')
E('contact.title', '<h1 class="main-title">', 'Prenons contact', 'Get in touch')
A('form.first', 'placeholder', 'Prénom', 'First name')
A('form.last', 'placeholder', 'Nom', 'Last name')
A('form.phone', 'placeholder', 'Téléphone', 'Phone')
E('form.privacy', '<label for="privacy-policy">', 'J’accepte', 'I accept the privacy policy')
E('form.send', '<button type="submit" class="contact-submit-btn">', 'Envoyer', 'Send')
E('advisor.eyebrow', '<h2 class="sub-title" style="text-align: left; margin-bottom: 10px;">', 'Conseil et vente', 'Advice &amp; sales')
E('advisor.text', '<p>', 'Silverpine SA est',
  'Silverpine SA is a Swiss family-owned investment company based in Nidwalden, developing premier real estate projects in the canton of Vaud and Central Switzerland. Each project is carried out with precision and commitment, ensuring steady progress, impeccable quality and complete transparency. At the heart of our philosophy are lasting relationships with our clients and partners, built on trust, integrity and collaboration. Our villas and apartments combine timeless architecture with modern comfort to create unique and inspiring places to live. Built with sustainable materials of the highest quality, they guarantee lasting value and exceptional well-being, for families and individuals alike.')
E('advisor.role', '<span>', 'Head of Projects', 'Head of Projects', fr='Responsable des projets')
E('partners', '<p>', 'PARTENAIRES', 'PARTNERS')
E('footer.privacy', '<a href="#" style="text-decoration:underline;">', 'Politique de', 'Privacy policy', fr='Politique de confidentialité')
A('lb.close', 'aria-label', 'Fermer la vue agrandie', 'Close enlarged view')
A('lb.alt', 'alt', 'Vue Agrandie', 'Enlarged view', fr='Vue agrandie')
E('lb.prev', '<button type="button" id="lightbox-prev" class="lightbox-nav-btn">', '&#10094;', '&#10094; Previous')
E('lb.next', '<button type="button" id="lightbox-next" class="lightbox-nav-btn">', 'Suivant', 'Next &#10095;')

# Genève row: the generic guard above can't match "Genève</td" inside the prefix; do it explicitly
errors = [e for e in errors if not e.startswith('E loc.geneva')]
FR.pop('loc.geneva', None); EN.pop('loc.geneva', None)
if src.count('<td>Genève</td>') == 1:
    src = src.replace('<td>Genève</td>', '<td data-i18n="loc.geneva">Genève</td>')
    FR['loc.geneva'], EN['loc.geneva'] = 'Genève', 'Geneva'
else:
    errors.append('loc.geneva not found exactly once')

# ------------------------------------------------------------------ write
if errors:
    print('\n'.join(errors))
    sys.exit(1)

src = src.replace('<html lang="fr-FR">', '<html lang="fr-CH">')
src = src.replace('  <script>\n    // 1. Header Shrink', '  <script src="js/i18n.js"></script>\n  <script>\n    // 1. Header Shrink', 1)
open(PATH, 'w', encoding='utf-8').write(src)

missing = sorted(set(FR) ^ set(EN))
assert not missing, missing
runtime = open('tools/i18n_runtime.js', encoding='utf-8').read()
js = ('/* Domaine de Bellevue - FR / EN translations.\n'
      ' * Edit text here: every key matches a data-i18n / data-i18n-attr attribute in index.html.\n'
      ' * Values may contain simple HTML (<br>, <strong>, &amp;). Attribute values (alt, title,\n'
      ' * placeholder, aria-label) must be plain text. */\n'
      'window.I18N = ' + json.dumps({'fr': FR, 'en': EN}, ensure_ascii=False, indent=2) + ';\n\n' + runtime)
open('js/i18n.js', 'w', encoding='utf-8').write(js)
print(f'OK: {len(FR)} keys; index.html tagged, js/i18n.js written')
