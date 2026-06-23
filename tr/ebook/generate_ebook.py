#!/usr/bin/env python3
"""
Pasifik’in Altındaki Mühür - EPUB Oluşturucu

Kullanım:
    pip install ebooklib
    python generate_ebook.py
"""

from ebooklib import epub
from pathlib import Path
import re

def clean_text(text):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#") or line.startswith("---") or not line:
            continue
        line = re.sub(r'[🌑]', '', line)
        line = ' '.join(line.split())
        lines.append(line)
    return '\n'.join(lines)

LICENSE_URL = 'https://creativecommons.org/licenses/by/4.0/'

# Telif/lisans sayfası — EPUB tek başına dağıtılsa bile lisans ve yazar görünür.
LICENSE_PAGE_HTML = f'''<h1>Pasifik’in Altındaki Mühür</h1>
<p><strong>Yazar / Author:</strong> Emre Ozudogru</p>
<p>© 2026 Emre Ozudogru</p>
<hr/>
<p><strong>Lisans:</strong> Bu eser Creative Commons Atıf 4.0 Uluslararası (CC BY 4.0)
lisansı ile lisanslanmıştır. Eseri özgürce okuyabilir, kopyalayabilir, dağıtabilir,
çevirebilir, uyarlayabilir ve ticari olarak kullanabilirsiniz — tek koşul, yazar adı
<strong>“Emre Ozudogru”</strong>nun korunması ve belirtilmesidir. Yazarlık silinemez
veya değiştirilemez.</p>
<p><strong>License:</strong> This work is licensed under a Creative Commons
Attribution 4.0 International License (CC BY 4.0). You are free to read, copy,
distribute, translate, adapt and use it commercially — on one condition: the author
name <strong>“Emre Ozudogru”</strong> must be preserved and attributed. Authorship
may not be removed or altered.</p>
<p>{LICENSE_URL}</p>
<p><em>Önerilen atıf / Suggested attribution:</em><br/>
“Pasifik’in Altındaki Mühür” by Emre Ozudogru, licensed under CC BY 4.0.</p>'''

def create_epub():
    book = epub.EpubBook()
    book.set_identifier('pasifik-muhur-2026')
    book.set_title('Pasifik’in Altındaki Mühür')
    book.set_language('tr')
    book.add_author('Emre Ozudogru')

    # Dublin Core lisans + telif metadata'sı (e-okuyucular ve kataloglar okur)
    book.add_metadata('DC', 'rights',
                      'CC BY 4.0 (Creative Commons Attribution 4.0 International). '
                      'Author "Emre Ozudogru" must be attributed. ' + LICENSE_URL)
    book.add_metadata('DC', 'publisher', 'Emre Ozudogru')
    book.add_metadata('DC', 'date', '2026')
    book.add_metadata(None, 'meta', '', {'name': 'dc.rights', 'content': LICENSE_URL})

    # Telif/lisans sayfası (kitabın ilk sayfası)
    license_page = epub.EpubHtml(title='Lisans / License', file_name='lisans.xhtml', lang='tr')
    license_page.content = LICENSE_PAGE_HTML
    book.add_item(license_page)

    chapters = []
    bolumler_dir = Path('../metin/bolumler')

    for i in range(1, 23):
        md_files = list(bolumler_dir.glob(f'{i:02d}-*.md'))
        if not md_files:
            continue

        content = md_files[0].read_text(encoding='utf-8')
        clean = clean_text(content)

        chapter = epub.EpubHtml(
            title=f'Bölüm {i}',
            file_name=f'bolum_{i:02d}.xhtml',
            lang='tr'
        )
        chapter.content = f'<h1>Bölüm {i}</h1><p>{clean.replace(chr(10), "</p><p>")}</p>'

        book.add_item(chapter)
        chapters.append(chapter)

    book.toc = [license_page] + chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav', license_page] + chapters

    output_path = Path('pasifik_muhur.epub')
    epub.write_epub(output_path, book, {})
    print(f'EPUB oluşturuldu: {output_path}')

if __name__ == '__main__':
    create_epub()