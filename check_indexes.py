import os
import re
from pathlib import Path

vault_path = r'C:\Users\emanu\OneDrive\Escritorio\USAC\Bóveda USAC'
md_files = list(Path(vault_path).rglob('*.md'))
relative_paths = set(str(p.relative_to(vault_path).with_suffix('')).replace('\\\\', '/') for p in md_files)
base_names = set(p.stem for p in md_files)

link_pattern = re.compile(r'\[\[(.*?)\]\]')

broken_links = []

for filepath in md_files:
    if not filepath.name.startswith('_Índice'):
        continue
        
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        continue
    
    links = link_pattern.findall(content)
    for link in links:
        target = link.split('|')[0]
        # if the table escaped it, it might end with \
        if target.endswith('\\'):
            target = target[:-1]
        target_file = target.split('#')[0].strip()
        
        if not target_file or target_file == '...':
            continue
            
        if target_file not in relative_paths and target_file not in base_names:
            broken_links.append((str(filepath.relative_to(vault_path)), target, link))

if broken_links:
    print('Broken links found in Indexes:')
    for file, target, original in broken_links:
        print(f'File: {file} -> Link: [[{original}]] (Target: {target} not found)')
else:
    print('All Index links are correct.')
