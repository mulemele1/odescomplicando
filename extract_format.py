#!/usr/bin/env python3
# coding: utf-8

import json

with open('odescomplicando.com/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar a seção relevante
idx = content.find('"Sou Engenheiro Informático com mais de 5 anos de experiência')

# Procurar o início da estrutura "a":{...}
section_start = content.rfind('"a":{', 0, idx)
print(f'Seção começaem: {section_start}')

# Extrair até encontrar a seção de formatação "B":[...]
b_start = content.find('"B":[', section_start)
print(f'Formatação B começa em: {b_start}')

# Extrair a seção de formatação (até o próximo "E":{})
b_section_start = b_start
b_snippet = content[b_start:b_start+2000]

# Encontrar onde termina
e_pos = b_snippet.find(',"E":{}')
b_section_full = b_snippet[:e_pos+7]

print('=== SEÇÃO DE FORMATAÇÃO (B) ===')
print(b_section_full[:1500])
print()
print(f'Total: {len(b_section_full)} caracteres')
