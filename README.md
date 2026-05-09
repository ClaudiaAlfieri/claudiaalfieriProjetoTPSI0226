# claudiaalfieriProjetoTPSI0226

# 🎬 PyFlix - Sistema de Gestão de Filmes e Séries

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![ATEC](https://img.shields.io/badge/Training-TPSI%20%7C%20ATEC-darkgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20progress-brightgreen?style=for-the-badge)

> Aplicação em Python desenvolvida como projeto final da disciplina de Programação do curso CET TPSI na ATEC.
> 
>  O PyFlix é um sistema de gestão pessoal de filmes e séries com interface em linha de comandos (CLI).

---

## 📌 Sobre o Projeto

O **PyFlix** foi desenvolvido como projeto final da unidade curricular de **Programação em Python** do programa **CET TPSI** na **ATEC — Training Academy**.

O objetivo é implementar um sistema de gestão completo com registo, validação, armazenamento e manipulação de dados de forma persistente, aplicando os conceitos lecionados ao longo do curso.

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 🔐 Autenticação | Login com validação de email e password por regex |
| 📋 Listagem | Visualização completa de todos os registos |
| ➕ Adicionar | Registo de novos filmes/séries com validação de dados |
| ✏️ Editar | Atualização de qualquer campo com validação |
| 🗑️ Apagar | Remoção com confirmação do utilizador |
| 🔍 Pesquisa Linear | Pesquisa por título — percorre a lista completa |
| 🔍 Pesquisa Binária | Pesquisa por ano — divide a lista ao meio (requer ordenação) |
| 📊 Bubble Sort | Ordenação por comparação de elementos vizinhos |
| 📊 Selection Sort | Ordenação por seleção do menor elemento |
| 📈 Estatísticas | Média, máximo/mínimo, total por tipo e filtros |
| 💾 Persistência | Dados guardados e carregados automaticamente em JSON |

---

## 🗂️ Estrutura do Projeto

```
pyflix/
├── main.py          # Ponto de entrada — coordena o programa
├── auth.py          # Autenticação e login
├── menus.py         # Interface de menus CLI
├── filmes.py        # Operações CRUD (criar, ler, editar, apagar)
├── data.py          # Persistência de dados em JSON
├── validate.py      # Validações com expressões regulares (regex)
├── search.py        # Algoritmos de pesquisa (linear e binária)
├── sort.py          # Algoritmos de ordenação (Bubble e Selection Sort)
└── estatisticas.py  # Estatísticas e filtros
```

---

## 🔐 Credenciais de Teste

```
Email:    admin@pyflix.com
Password: Admin123
```

---

## ▶️ Como Executar

1. Clona o repositório:
```bash
git clone https://github.com/ClaudiaAlfieri/claudiaalfieriProjetoTPSI0226.git
```

2. Entra na pasta do projeto:
```bash
cd claudiaalfieriProjetoTPSI0226
```

3. Executa o programa:
```bash
python main.py
```

> Não são necessárias instalações adicionais — o projeto usa apenas bibliotecas nativas do Python (`json`, `re`).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **JSON** — persistência de dados
- **Regex (re)** — validação de email, password e data
- **Git** — controlo de versão
- **GitHub** — repositório remoto

---

## 📐 Conceitos Aplicados

| Conceito | Descrição |
|---|---|
| 🧩 Modularização | 9 ficheiros com responsabilidades separadas |
| 🔎 Pesquisa Linear | Percorre a lista completa elemento a elemento |
| 🔎 Pesquisa Binária | Divide a lista ao meio a cada comparação |
| 📊 Bubble Sort | Compara e troca elementos vizinhos sucessivamente |
| 📊 Selection Sort | Procura o menor elemento e coloca-o na posição correta |
| ✅ Regex | Validação de formato de email, password e data |
| 💾 Persistência JSON | Dados carregados ao iniciar e guardados ao sair |
| ⚠️ Exceções | Tratamento de erros com try/except em operações de ficheiros |

---

## 👩‍💻 Autora

Este projeto foi desenvolvido por **Cláudia Alfieri** como projeto final da disciplina de Programação em Python do curso CET TPSI na ATEC.

---

Feito com ❤️, muitos `print()` e algum `try/except` pelo caminho 🐍🚀
