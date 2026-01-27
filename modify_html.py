#!/usr/bin/env python3
# coding: utf-8

with open('odescomplicando.com/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar o parágrafo
idx = content.find('"Sou Engenheiro Informático com mais de 5 anos de experiência')
offset_minha = 442

# Encontrar a seção inteira de "a":{...}
section_start = content.rfind('"a":{', 0, idx)
section_end = content.find(',"E":{}', section_start) + len(',"E":{}')

print(f'Seção do parágrafo: posição {section_start} a {section_end}')

# Extrair a seção completa
section = content[section_start:section_end]

# Salvar backup
with open('backup.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Backup criado em backup.html')
print()

# Agora preciso modificar a seção "B":[] para adicionar formatação de cor branca
# A estrutura atual termina com:
# {"A?":"B","A":77},{"A?":"A","A":{"leading":{"B":"1500.0"},"font-size":{"B":"20.4076"}}},
# {"A?":"B","A":1},{"A?":"A","A":{...all empty...}},{"A?":"B","A":1},{"A?":"A","A":{...all empty...}}]

# Preciso inserir antes do último elemento:
# {"A?":"B","A":442},{"A?":"A","A":{"color":{"B":"#ffffff"}}}

# Vamos procurar a posição correta para inserção
b_start = section.find('"B":[')
b_section = section[b_start:]

# Encontrar o último {"A?":"B" antes do fechamento do array
last_b_marker = b_section.rfind('{"A?":"B"')
print(f'Último marcador B encontrado em posição relativa: {last_b_marker}')

# Vamos ser mais preciso: procurar a estrutura exata
# Procurar: {"A?":"B","A":77},{"A?":"A",...}}},
# E inserir nela nossa formatação

# Vamos extrair a parte B inteira para análise
b_end = b_section.find('],"E":{}')
b_content = b_section[:b_end]

print()
print('=== Últimos 500 caracteres de B ===')
print(b_content[-500:])
print()

# Agora vamos fazer a modificação
# Preciso encontrar um ponto seguro para inserir

# A estrutura termina com:
# [...},{"A?":"B","A":1},{"A?":"A","A":{...empty...}}]

# Vou inserir antes do último ]
# Especificamente antes do último }]

# Encontrar a posição
insert_point = b_content.rfind('}]')
if insert_point == -1:
    insert_point = b_content.rfind(']')

print(f'Ponto de inserção (relativo): {insert_point}')

# Criar a nova formatação
new_format = ',{"A?":"B","A":442},{"A?":"A","A":{"color":{"B":"#ffffff"}}}'

# Aplicar a mudança
new_b_section = b_content[:insert_point] + new_format + b_content[insert_point:]

# Atualizar a seção
new_section = section[:b_start] + new_b_section + section[b_start + len(b_section) + 8:]

# Atualizar o arquivo
new_content = content[:section_start] + new_section + content[section_end:]

# Salvar o arquivo modificado
with open('odescomplicando.com/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print()
print('✓ Arquivo modificado com sucesso!')
