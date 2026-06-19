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

def create_epub():
    book = epub.EpubBook()
    book.set_identifier('pasifik-muhur-2026')
    book.set_title('Pasifik’in Altındaki Mühür')
    book.set_language('tr')
    book.add_author('Emre Ozudogru')

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

    book.toc = chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav'] + chapters

    output_path = Path('pasifik_muhur.epub')
    epub.write_epub(output_path, book, {})
    print(f'EPUB oluşturuldu: {output_path}')

if __name__ == '__main__':
    create_epub()