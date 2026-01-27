#!/usr/bin/env python3
# coding: utf-8

with open('odescomplicando.com/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Procurar texto
idx = content.find('Sou Engenheiro Informático com mais de 5 anos de experiência')
idx2 = content.find('Minha paixão por compartilhar')

print(f'Pos Sou: {idx}')
print(f'Pos Minha: {idx2}')

if idx != -1 and idx2 != -1:
    offset = idx2 - idx
    print(f'OFFSET: {offset}')
