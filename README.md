# StudyFlow CLI

Aplicação em linha de comando desenvolvida para ajudar estudantes a organizar sua rotina de estudos de forma simples, prática e acessível.

## Problema real
Muitos estudantes têm dificuldade para manter uma rotina organizada de estudos, lembrar tarefas pendentes e acompanhar o que já foi concluído. Isso pode prejudicar o aprendizado, a disciplina e a produtividade.

## Proposta da solução
O StudyFlow CLI oferece um gerenciador simples de tarefas de estudo com interface de terminal. O usuário pode cadastrar, listar, concluir e remover tarefas, mantendo uma rotina mais organizada sem depender de ferramentas complexas.

## Público-alvo
- Estudantes do ensino médio, técnico ou superior
- Pessoas com dificuldade para manter rotina de estudos
- Usuários que preferem soluções simples em terminal

## Funcionalidades principais
- Adicionar tarefa de estudo
- Listar tarefas cadastradas
- Marcar tarefa como concluída
- Remover tarefa
- Salvar tarefas em arquivo JSON

## Tecnologias utilizadas
- Python 3
- Pytest
- Ruff
- GitHub Actions
- JSON

## Estrutura do projeto
```bash
studyflow-cli/
├── src/
├── tests/
├── data/
├── .github/workflows/
├── README.md
├── requirements.txt
├── VERSION
├── CHANGELOG.md
└── .gitignore
```

## Instalação
```bash
!Execute no Power Shell ou no CMD do Linux!

git clone https://github.com/ArthurNeiva017/studyflow.git
cd studyflow-cli
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Execução
```bash
python src/main.py
```

## Como usar
Ao executar o programa, o usuário verá um menu com as opções:

```text
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair
```

## Executar os testes
```bash
pytest
```

## Executar o lint
```bash
ruff check .
```
## Versão do Projeto

O projeto utiliza versionamento semântico no formato MAJOR.MINOR.PATCH.

Versão atual: **1.0.0**

A versão está declarada no arquivo `pyproject.toml` e também no arquivo `VERSION`.

## Autor
Arthur Barroso Neiva


