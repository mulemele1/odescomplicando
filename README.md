# A Tecnologia

Website do projeto A Tecnologia - especializado em desvendar os mistérios da TI.

## Como executar localmente

### Pré-requisitos
- Node.js 14+ instalado ([baixar aqui](https://nodejs.org/))

### Instalação e execução

1. **Clone ou navegue até a pasta do projeto:**
```bash
cd "d:\JACINTO JOB\TRABALHO JACINTO\PROGRAMACAO\Profissional"
```

2. **Instale as dependências (se necessário):**
```bash
npm install
```

3. **Inicie o servidor:**
```bash
npm start
```

4. **Abra no navegador:**
```
http://localhost:3000
```

O servidor estará disponível em `http://localhost:3000` e servirá os arquivos da pasta `odescomplicando.com`.

## Deploy no Vercel

### Passo 1: Criar repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique em "New" para criar um novo repositório
3. Nome: `odescomplicando` (ou outro nome de sua preferência)
4. Selecione "Public" para ser gratuito
5. Clique em "Create repository"

### Passo 2: Fazer push do código para GitHub

No PowerShell, dentro da pasta do projeto:

```bash
# Inicializar git (se ainda não está)
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit - A Tecnologia website"

# Adicionar remote (substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/odescomplicando.git

# Enviar para GitHub (primeira vez)
git branch -M main
git push -u origin main
```

### Passo 3: Deploy no Vercel

1. Acesse [vercel.com](https://vercel.com)
2. Clique em "Sign Up" e conecte com sua conta GitHub
3. Clique em "New Project"
4. Selecione o repositório `odescomplicando`
5. Vercel detectará automaticamente a configuração
6. Clique em "Deploy"

Seu site estará disponível em: `https://seu-site.vercel.app`

## Estrutura do projeto

```
├── server.js           # Servidor Node.js
├── package.json        # Dependências do projeto
├── vercel.json         # Configuração do Vercel
├── .gitignore          # Arquivos a ignorar no git
├── README.md           # Este arquivo
└── odescomplicando.com/
    ├── index.html      # Página principal
    └── _assets/        # CSS, JS, imagens, etc.
```

## Notas

- O site é uma cópia espelhada (mirror) feita com HTTrack
- Para produção, considere otimizar as imagens e remover arquivos desnecessários
- Verifique as permissões de copyright e licença do site original

---

Desenvolvido com ❤️
