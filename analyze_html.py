#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

# Ler o arquivo
with open('odescomplicando.com/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar o texto
sou_idx = content.find('"Sou Engenheiro Informático')
minha_idx = content.find('Minha paixão', sou_idx)

if sou_idx != -1 and minha_idx != -1:
    # Calcular a posição dentro do bloco de texto
    # Precisamos contar a partir do início de "Sou"
    # No JSON, o texto está dentro de "A":"Sou Engenheiro..."
    # Vamos extrair desde o início da string até "Minha paixão"
    
    start_quote = content.rfind('"A":"Sou Engenheiro', 0, sou_idx)
    full_text_start = start_quote + 5  # Posição após "A":"
    
    # Encontrar onde "Minha paixão" começa (relativamenteat "Sou")
    char_offset = minha_idx - full_text_start
    
    print(f"Posição 'Sou Engenheiro' no arquivo: {sou_idx}")
    print(f"Posição 'Minha paixão' no arquivo: {minha_idx}")
    print(f"Início da string (após 'A\":'): {full_text_start}")
    print(f"OFFSET DO 'Minha paixão' a partir de 'Sou': {char_offset}")
    print()
    
    # Extrair o texto para visualizar
    text_snippet = content[full_text_start:minha_idx+100]
    print("Texto:")
    print(text_snippet)
    print()
    
    # Agora procurar pela seção de formatação (B)
    # A estrutura é: "B":[{...}]
    b_start = content.find('"B":[', sou_idx)
    b_end = content.find('],"', b_start) + 1
    
    if b_start != -1 and b_end != -1:
        formatting_section = content[b_start:b_end+100]
        print("Seção de formatação (primeiros 500 chars):")
        print(formatting_section[:500])
        print()
        print(f"Offset 'Minha paixão' para inserir formatação: {char_offset}")
