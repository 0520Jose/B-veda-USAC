import os
import re
from pathlib import Path
import urllib.parse

vault_path = Path(r'C:\Users\emanu\OneDrive\Escritorio\USAC\Bóveda USAC')
md_files = list(vault_path.rglob('*.md'))

# build lookup sets
relative_paths = set(p.relative_to(vault_path).as_posix() for p in md_files)
base_names_to_rel = {p.stem: p.relative_to(vault_path).as_posix() for p in md_files}

link_pattern = re.compile(r'\[\[(.*?)\]\]')

broken_links = []
uncreated_concepts = set()

for filepath in md_files:
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        continue
    
    links = link_pattern.findall(content)
    for link in links:
        target = link.split('|')[0]
        if target.endswith('\\'):
            target = target[:-1]
        target_file = target.split('#')[0].strip()
        
        if not target_file or target_file == '...':
            continue
            
        # 1. Check if target_file is an exact match for a relative path (without .md)
        if target_file + '.md' in relative_paths:
            continue
            
        # 2. Check if target_file matches a base name
        if target_file in base_names_to_rel:
            continue
            
        # 3. Check if target_file matches a relative path from the current file's directory
        rel_from_curr = (filepath.parent / (target_file + '.md')).resolve()
        try:
            if rel_from_curr.relative_to(vault_path).as_posix() in relative_paths:
                continue
        except ValueError:
            pass
            
        # If it's not an index, maybe it's just an uncreated concept tag like [[Cloud Computing]]
        if not filepath.name.startswith('_Índice'):
            uncreated_concepts.add(target_file)
            continue
            
        broken_links.append((filepath.relative_to(vault_path).as_posix(), target, link))

print('--- Broken Links in Indexes ---')
for f, t, o in broken_links:
    print(f"{f}: [[{o}]]")
print('--- Uncreated Concepts in Notes ---')
print(f"Total uncreated concept links: {len(uncreated_concepts)}")
