import json
import re

with open('odescomplicando.com/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Procurar o índice exato do texto "Minha paixão"
# Precisamos encontrar onde no parágrafo ele começa
pattern1 = 'Sou Engenheiro Informßtico com mais'
pattern2 = 'Minha paixÒo por compartilhar'

idx1 = content.find(pattern1)
idx2 = content.find(pattern2, idx1)

if idx1 != -1 and idx2 != -1:
    # Calcular o offset
    offset = idx2 - idx1
    print(f'OFFSET: {offset}')
    
    # Agora vamos procurar pela estrutura JSON para modificar
    # Procurar {"A?":"B","A":250} para adicionar formatação
    
    # Extrair a seção relevante
    # Encontrar o início da seção "a":{...}
    section_start = content.rfind('"a":{', 0, idx1)
    
    # Encontrar o fim da seção (próximo "E":{})
    section_end = content.find('"E":{}}', section_start) + len('"E":{}}')
    
    if section_start != -1 and section_end != -1:
        section = content[section_start:section_end]
        
        # Salvar seção para análise
        with open('section_backup.txt', 'w', encoding='utf-8') as f:
            f.write(section)
        
        print(f'Seção extraída: {len(section)} caracteres')
        
        # Buscar pela estrutura "B":[...] para ver as formatações
        b_start = section.find('"B":[')
        b_snippet = section[b_start:b_start+1000]
        
        with open('formatting_snippet.txt', 'w', encoding='utf-8') as f:
            f.write(b_snippet)
        
        print('Arquivos salvos: section_backup.txt e formatting_snippet.txt')
else:
    print('Padrões não encontrados')
