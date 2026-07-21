import os
import re
from pathlib import Path

vault_path = r'C:\Users\emanu\OneDrive\Escritorio\USAC\Bóveda USAC'
md_files = list(Path(vault_path).rglob('*.md'))
# Build a set of all relative paths (without .md) and all base names (without .md)
relative_paths = set(str(p.relative_to(vault_path).with_suffix('')).replace('\\\\', '/') for p in md_files)
base_names = set(p.stem for p in md_files)

link_pattern = re.compile(r'\[\[(.*?)\]\]')

broken_links = []

for filepath in md_files:
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        continue
    
    links = link_pattern.findall(content)
    for link in links:
        # link can be 'Path/To/File|Alias' or 'File|Alias'
        target = link.split('|')[0]
        # target might have heading like 'File#Heading'
        target_file = target.split('#')[0].strip()
        
        if not target_file:
            continue
            
        # check if it exists in relative paths or base names
        if target_file not in relative_paths and target_file not in base_names:
            broken_links.append((str(filepath.relative_to(vault_path)), target, link))

if broken_links:
    print('Broken links found:')
    for file, target, original in broken_links:
        print(f'File: {file} -> Link: [[{original}]] (Target: {target} not found)')
else:
    print('No broken links found.')
